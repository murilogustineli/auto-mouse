import pyautogui
import time
import random


# Function to keep moving the mouse automatically
def move_mouse(wait_time=1):
    count = 0
    while True:
        # current mouse positions
        x, y = pyautogui.position()
        # Move mouse
        if count % 2 == 0:
            pyautogui.moveTo(x + 10, y)
        else:
            pyautogui.moveTo(x - 10, y)
        time.sleep(wait_time)  # replace 1 with the number of seconds you want to wait
        count += 1


# Run function
if __name__ == "__main__":
    move_mouse()
