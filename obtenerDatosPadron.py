import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog



def scrape_pami_page(beneficio, parent):
    # Construir la URL con los parámetros proporcionados
    url = f"https://prestadores.pami.org.ar/result.php?c=6-2-1-1&beneficio={beneficio}&parent={parent}&vm=2"

    # Realizar la solicitud GET a la URL
    response = requests.get(url)
    
    # Comprobar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Analizar el contenido HTML de la página
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Encontrar el nombre y apellido del beneficiario
        nombre_apellido_tag = soup.find('td', class_='grisClaro').find_all('p')[0]
        nombre_apellido = nombre_apellido_tag.text.strip()
        
        # Encontrar la UGL del beneficiario
        ugl_tag = soup.find('td', string='UGL:')
        if ugl_tag:
            ugl = ugl_tag.find_next_sibling('td').text.strip()
        else:
            ugl = "No especificada"
        
        # Imprimir el nombre, apellido y UGL
        if (nombre_apellido!=''):
            print(f"Beneficio: {beneficio}, UGL: {ugl}")
            return (nombre_apellido!='')
        else:
            False
            
    else:
        print("No se pudo obtener la página")
        return False

def ejecutar_scraping():
    filename = filedialog.askopenfilename()  # Solicitar al usuario que seleccione el archivo
    encontrados = 0

    with open(filename, 'r') as file:
        lineas = file.readlines()

    # Iterar sobre las líneas del archivo
    for linea in lineas:
        # Ejemplo de uso
        beneficio = linea.strip().split(',')[0]

        # Extraer los últimos dos dígitos del beneficio para asignarlos al parentesco
        parent = beneficio[-2:]

        # Eliminar los últimos dos dígitos del beneficio
        beneficio = beneficio[:-2]

        if scrape_pami_page(beneficio, parent):
            encontrados += 1
        else:
            with open('resultadosPADRON.txt', 'a') as result_file:
                result_file.write(f"{linea.strip()} - NO ENCONTRADO\n")

    with open('resultadosPADRON.txt', 'a') as result_file:
                result_file.write(f"{encontrados} - TOTAL ENCONTRADOS\n")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Scraping de Beneficios PAMI")

# Botón para seleccionar el archivo
archivo_button = tk.Button(root, text="Seleccionar Archivo", command=ejecutar_scraping)
archivo_button.pack(pady=20)

root.mainloop()
