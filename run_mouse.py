import pyautogui
import time


# Function to keep moving the mouse automatically
def move_mouse():
    # current mouse positions
    x, y = pyautogui.position()
    pyautogui.moveTo(x + 5, y + 5)

while True:
    move_mouse()
    time.sleep(5)  # replace 5 with the number of seconds you want to wait
