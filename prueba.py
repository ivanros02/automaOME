import pyautogui
import time

time.sleep(5)

try:
        # Intentar encontrar una de las imágenes de error
        x_error, y_error = pyautogui.locateCenterOnScreen('omeYaGeneradaError521001.png', confidence=0.9)

        
except pyautogui.ImageNotFoundException:
        
        try:
            # Intentar con la otra imagen de error
            x_error, y_error = pyautogui.locateCenterOnScreen('omeYaGeneradaError520101.png', confidence=0.9)
            print(f"Error encontrado en el número:1 ")
            pyautogui.press('tab')  # cerrar verificación
            time.sleep(3)
        except pyautogui.ImageNotFoundException:
            pyautogui.press('tab')  # cerrar verificación
            pyautogui.press('enter')
            print(f"Error encontrado en el número:2")
            pass  # Si ninguna de las imágenes de error se encuentra, simplemente continuar sin imprimir nada
print('paso')
