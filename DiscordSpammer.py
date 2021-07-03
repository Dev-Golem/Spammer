#Make sure to pip install pyautogui before running

import pyautogui, time

time.sleep(1)
file_name = "beemovie"

f = open(file_name, 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
