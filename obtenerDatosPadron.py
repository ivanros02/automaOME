import requests
from bs4 import BeautifulSoup

encontrados=0

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
        
        # Retornar el nombre, apellido y UGL
        return nombre_apellido, ugl
    else:
        print("No se pudo obtener la página")

with open('beneficios.txt', 'r') as file:
    lineas = file.readlines()

# Iterar sobre las líneas del archivo
for linea in lineas:
    # Ejemplo de uso
    beneficio =linea.strip()

# Extraer los últimos dos dígitos del beneficio para asignarlos al parentesco
    parent = beneficio[-2:]

# Eliminar los últimos dos dígitos del beneficio
    beneficio = beneficio[:-2]

    nombre_apellido = scrape_pami_page(beneficio, parent)
    if nombre_apellido!=('', ''):
        encontrados = encontrados+1
    else:
        print(f"Beneficio no encontrado:{beneficio}")

print(encontrados)


