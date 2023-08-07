import pyautogui
import time
import random


# Function to keep moving the mouse automatically
def move_mouse(wait_time=1):
    while True:
        # current mouse positions
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 10, y)
        time.sleep(wait_time)  # replace 1 with the number of seconds you want to wait
        pyautogui.moveTo(x - 10, y)
        time.sleep(wait_time)
    # rand = random.randint(1, 100)
    # if 0 < rand <= 25:
    #     pyautogui.moveTo(x + 10, y + 10)
    # elif 25 < rand <= 50:
    #     pyautogui.moveTo(x + 10, y - 10)
    # elif 50 < rand <= 75:
    #     pyautogui.moveTo(x - 10, y + 10)
    # elif 75 < rand <= 100:
    #     pyautogui.moveTo(x - 10, y - 10)

if __name__ == "__main__":
    move_mouse()
