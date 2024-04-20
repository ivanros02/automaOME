import pyautogui
import time

# Definir una lista de tuplas que contienen las horas y minutos deseados
horas_y_minutos = [('08', '0'), ('08', '30'), ('09', '0'), ('09', '30'), ('10', '0'), 
                   ('10', '30'), ('11', '0'), ('11', '30'), ('12', '0'), ('12', '30'), 
                   ('13', '0'), ('13', '30'), ('14', '0')]

usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")
aceptador = input("elegir psicologo o clinica: ")


if aceptador=="psicologo":
   cantAOme= 2
   cantABenef = 11
else:
   cantAOme =3
   cantABenef = 13


pyautogui.press('win')
time.sleep(2)
# Entrar a pagina CUP
pyautogui.write('https://cup.pami.org.ar/controllers/loginController.php')
time.sleep(1)
pyautogui.press('enter')

# Esperar unos segundos para que la página cargue completamente
time.sleep(5)
pyautogui.hotkey('ctrl','a')
pyautogui.press('del')
# Usar PyAutoGUI para enviar las teclas necesarias para ingresar al sitio web
pyautogui.typewrite(usuario)  # Reemplaza 'usuario' por tu nombre de usuario
pyautogui.press('tab')  # Cambia el foco al campo de contraseña
time.sleep(2)
pyautogui.typewrite(contrasena)  # Reemplaza 'contraseña' por tu contraseña
time.sleep(2)
pyautogui.press('enter')  # Presiona la tecla Enter para enviar el formulario

# Esperar unos segundos para asegurarse de que la página haya cargado completamente
time.sleep(10)
#pyautogui.click(145,118) #Boton OME
pyautogui.press('tab',presses=cantAOme) #3 veces a buscar el boton ome

pyautogui.press('enter') # en boton ome 

time.sleep(3)

# Leer el archivo de texto y obtener las líneas
with open('aRealizar.txt', 'r') as file:
   lineas = file.readlines()

#Iterar sobre las líneas del archivo y las horas y minutos deseados
for i, linea in enumerate(lineas):
   # Calcular el índice de la lista de horas y minutos utilizando el operador de módulo
   indice = i % len(horas_y_minutos)
   hora, minuto = horas_y_minutos[indice]
   pyautogui.press('tab',presses=cantABenef)
   pyautogui.hotkey('ctrl','a')
   pyautogui.press('del')
   pyautogui.typewrite(linea.strip())  # Utiliza la línea actual del archivo
   time.sleep(1)

   pyautogui.press('tab',presses=9) #hasta el boton buscar
   pyautogui.press('enter')
   time.sleep(4)
   pyautogui.press('tab',presses=22)#llegar hasta ver las omes generadas para beneficio
   pyautogui.press('down')
   pyautogui.press('down')
   pyautogui.press('down')
   time.sleep(3)
   
   try:
      x, y = pyautogui.locateCenterOnScreen('./img/botonValidar.png',confidence=0.9) #click en validar
      pyautogui.click(x, y)
      time.sleep(4)
      pyautogui.press('tab',presses=3) #llegar a fecha
      pyautogui.press('enter') #pone la fecha actual por defecto
      time.sleep(1)
      x, y = pyautogui.locateCenterOnScreen('./img/horario.png',confidence=0.7) #click en horario
      pyautogui.click(x, y)
      pyautogui.typewrite(hora)#hora
      pyautogui.press('tab')
      pyautogui.press('tab')
      pyautogui.typewrite(minuto)#minutos
      pyautogui.press('tab')
      pyautogui.press('tab') #hasta boca de atencion
      pyautogui.press('c') # primera boca

      pyautogui.press('tab') # hasta aceptar
      pyautogui.press('enter') # acepto
      time.sleep(3)
      pyautogui.press('enter') #para aceptar
        # Escribir en el archivo que la línea fue aceptada
      with open('resultadosACEPTACION.txt', 'a') as result_file:
         result_file.write(f"{linea.strip()} - Aceptada\n")
      time.sleep(5)
     

  
   except pyautogui.ImageNotFoundException:
      pyautogui.press('up')
      pyautogui.press('up')
      pyautogui.press('up')
      pyautogui.press('up')
      time.sleep(1)
      x, y = pyautogui.locateCenterOnScreen('./img/panelAceptaction.png',confidence=0.7) #click en horario
      pyautogui.click(x, y)
      with open('resultadosACEPTACION.txt', 'a') as result_file:
         result_file.write(f"{linea.strip()} - No Aceptada\n")
      time.sleep(2)
      
      pass
  
   
