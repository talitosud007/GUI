import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press('win')
time.sleep(1)
pyautogui.write('chrome')
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)

pyautogui.write('https://www.google.com')
pyautogui.press('enter')
time.sleep(5)

pyautogui.write('Clima hoje na minha cidade')
pyautogui.press('enter')
time.sleep(6)

screenshot = pyautogui.screenshot()
screenshot.save('previsao.png')

print('Print salvo como previsao.png')
