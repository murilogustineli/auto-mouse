import pyautogui
import time
import random


# Function to keep moving the mouse automatically
def move_mouse():
    # current mouse positions
    x, y = pyautogui.position()
    rand = random.randint(1, 100)
    if 0 < rand <= 25:
        pyautogui.moveTo(x + 10, y + 10)
    elif 25 < rand <= 50:
        pyautogui.moveTo(x + 10, y - 10)
    elif 50 < rand <= 75:
        pyautogui.moveTo(x - 10, y + 10)
    elif 75 < rand <= 100:
        pyautogui.moveTo(x - 10, y - 10)

while True:
    move_mouse()
    time.sleep(1)  # replace 5 with the number of seconds you want to wait
