import pyautogui
import time

time.sleep(5)

x, y = pyautogui.locateCenterOnScreen('./img/pruebaIMG.png',confidence=0.7) #click en validar
pyautogui.click(x, y)