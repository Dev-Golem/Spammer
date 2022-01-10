#Make sure to pip install pyautogui before running

import pyautogui, time

time.sleep(1)
file_name = input("Whats the name of the file?: ")

f = open(file_name, 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
