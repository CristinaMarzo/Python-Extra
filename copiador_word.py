import pyautogui

def copiarword():
#bucle
    pyautogui.PAUSE=5

    pyautogui.moveTo(x=305, y=315)
    pyautogui.click()
    pyautogui.dragTo(385, 721, 5, button='left')
    while (pyautogui.dragTo(385, 721, 5, button='left')):
        pyautogui.scroll(-400)
    pyautogui.dragTo(1119, 720, 6, button='left')

    pyautogui.moveTo(x=83, y=102)
    pyautogui.click()

    pyautogui.PAUSE=10

    pyautogui.moveTo(x=27, y=89)
    pyautogui.click()
    
copiarword()
