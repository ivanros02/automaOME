import pyautogui
import time
import random

# Solicitar los datos al usuario por consola
practica = input("Ingrese practica: ")
usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")

# Inicializar la lista de códigos de diagnóstico
codigos_diagnosticos = []

# Verificar el valor de 'practica' y ajustar 'codigos_diagnosticos' en consecuencia
if practica == '521001':
    codigos_diagnosticos = ['F99', 'F41', 'F413', 'F429']
elif practica == '520101':
    codigos_diagnosticos = ['F88', 'F89']

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

# Leer el archivo de texto y obtener las líneas
with open('beneficios.txt', 'r') as file:
    lineas = file.readlines()

# Iterar sobre las líneas del archivo
for linea in lineas:
    x, y = pyautogui.locateCenterOnScreen('beneficioGENERAR.png')  # beneficio
    pyautogui.click(x, y)
    pyautogui.typewrite(linea.strip())  # Utiliza la línea actual del archivo
    time.sleep(1)

    pyautogui.press('tab')  # para buscar beneficio anterior
    time.sleep(1)

    pyautogui.press('tab', presses=6)  # hasta diag
    codigo_aleatorio = random.choice(codigos_diagnosticos)
    pyautogui.typewrite(codigo_aleatorio)
    time.sleep(3)
    pyautogui.press('enter')

    pyautogui.press('tab', presses=6)  # hasta práctica
    pyautogui.typewrite(practica)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.press('tab', presses=14)  # hasta finalizar
    pyautogui.press('enter')
    time.sleep(3)

    pyautogui.press('tab', presses=3)  # hasta confirmar ome
    pyautogui.press('enter')
    time.sleep(5)

    pyautogui.press('tab')  # cerrar verificación
    pyautogui.press('enter')

    pyautogui.press('up', presses=4)  # ir hasta arriba de la página
    time.sleep(3)
