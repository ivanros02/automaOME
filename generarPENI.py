import pyautogui
import time
import tkinter as tk
from tkinter import filedialog

def ejecutar():
    # Obtener los valores de la interfaz
    practica = practica_var.get()
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()
    
    # Cargar el archivo seleccionado
    filename = filedialog.askopenfilename()
    # Reemplazar los puntos por una cadena vacía en el archivo de entrada
    with open(filename, 'r') as file:
        data = file.read()
    data_sin_puntos = data.replace('.', '')
    with open(filename, 'w') as file:
        file.write(data_sin_puntos)

    # Leer el archivo modificado
    with open(filename, 'r') as file:
        lineas = file.readlines()

    generadas = 0

    time.sleep(2)
    pyautogui.press('win')
    time.sleep(2)
    # Entrar a página CUP
    pyautogui.write('https://cup.pami.org.ar/controllers/loginController.php')
    time.sleep(1)
    pyautogui.press('enter')

    # Esperar unos segundos para que la página cargue completamente
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('del')
    # Usar PyAutoGUI para enviar las teclas necesarias para ingresar al sitio web
    pyautogui.typewrite(usuario)
    pyautogui.press('tab')  # Cambiar el foco al campo de contraseña
    time.sleep(2)
    pyautogui.typewrite(contrasena)
    time.sleep(2)
    pyautogui.press('enter')  # Presionar Enter para enviar el formulario

    # Esperar unos segundos para asegurarse de que la página haya cargado completamente
    time.sleep(5)
    pyautogui.press('tab', presses=3)  # 3 veces para buscar el botón ome
    pyautogui.press('enter')  # en boton ome
    time.sleep(3)

    # Iterar sobre las líneas del archivo
    for linea in lineas:
        time.sleep(1)
        numero, codigo = linea.strip().split(",")
        x, y = pyautogui.locateCenterOnScreen('./img/botonOme.png',confidence=0.7) #click en validar
        pyautogui.click(x, y)
        time.sleep(5)
        pyautogui.press('tab',presses=10)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('del')
        time.sleep(1)
        pyautogui.typewrite(numero)  # Utiliza la línea actual del archivo
        time.sleep(1)

        pyautogui.press('tab')  # para buscar beneficio anterior
        time.sleep(4)

        pyautogui.press('tab', presses=6)  # hasta diag
        pyautogui.typewrite(codigo)
        time.sleep(3)
        pyautogui.press('enter')

        pyautogui.press('tab', presses=6)  # hasta práctica
        pyautogui.typewrite(practica)
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.press('tab', presses=14)  # hasta finalizar
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(4)

        pyautogui.press('tab', presses=3)  # hasta confirmar ome
        pyautogui.press('enter')
        time.sleep(5)
        
        # Validar si la orden fue generada correctamente
        try:
            pyautogui.locateCenterOnScreen('./img/ordenGenerada.png',confidence=0.7)
            generadas += 1
            with open('resultadosGENERACION.txt', 'a') as result_file:
                result_file.write(f"{linea.strip()} - GENERADA\n")
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.press('up', presses=4)
            time.sleep(1)
        except pyautogui.ImageNotFoundException:
            with open('resultadosGENERACION.txt', 'a') as result_file:
                result_file.write(f"{linea.strip()} - NO GENERADA\n")
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.press('up', presses=4)
            time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen('./img/eliminarDiag.png')  # beneficio
            pyautogui.doubleClick(x, y)
            pass

        print(generadas)



# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Automatización de Proceso")

# Etiqueta y entrada para el campo de usuario
usuario_label = tk.Label(root, text="Usuario:")
usuario_label.grid(row=0, column=0, padx=5, pady=5)
usuario_entry = tk.Entry(root)
usuario_entry.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta y entrada para el campo de contraseña
contrasena_label = tk.Label(root, text="Contraseña:")
contrasena_label.grid(row=1, column=0, padx=5, pady=5)
contrasena_entry = tk.Entry(root, show="*")
contrasena_entry.grid(row=1, column=1, padx=5, pady=5)

# Etiqueta y menú desplegable para el campo de práctica
practica_label = tk.Label(root, text="Práctica:")
practica_label.grid(row=2, column=0, padx=5, pady=5)
practica_var = tk.StringVar(root)
practica_var.set("520101")  # Valor por defecto
practica_menu = tk.OptionMenu(root, practica_var, "520101", "521001")
practica_menu.grid(row=2, column=1, padx=5, pady=5)

# Botón para seleccionar el archivo
archivo_button = tk.Button(root, text="Seleccionar Archivo", command=ejecutar)
archivo_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

