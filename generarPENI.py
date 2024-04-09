import pyautogui
import time

# Solicitar los datos al usuario por consola
practica = input("Ingrese practica  520101 o 521001: ")
usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")
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

# Leer el archivo de texto y obtener las líneas
with open('beneficiosYDiag.txt', 'r') as file:
    lineas = file.readlines()

# Iterar sobre las líneas del archivo
for linea in lineas:
    numero, codigo = linea.strip().split(",")  # Dividir la línea en número y código
    x, y = pyautogui.locateCenterOnScreen('beneficioGENERAR.png',confidence=0.7)  # beneficio
    pyautogui.doubleClick(x, y)
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
        pyautogui.locateCenterOnScreen('ordenGenerada.png', confidence=0.7)
        generadas += 1
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('up', presses=4)
        time.sleep(1)
    except pyautogui.ImageNotFoundException:
        print(f'{numero} ya generada')
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('up', presses=4)
        time.sleep(1)
        x, y = pyautogui.locateCenterOnScreen('eliminarDiag.png',confidence=0.7)  # beneficio
        pyautogui.doubleClick(x, y)

print(generadas)

