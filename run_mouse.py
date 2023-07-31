import pyautogui
import time
import random


# Function to keep moving the mouse automatically
def move_mouse():
    # current mouse positions
    x, y = pyautogui.position()
    rand = random.randint(1, 10)
    pyautogui.moveTo(x + rand, y + rand)

while True:
    move_mouse()
    time.sleep(1)  # replace 5 with the number of seconds you want to wait
