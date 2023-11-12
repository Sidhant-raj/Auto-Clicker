import pyautogui
import keyboard
import win32api
import time

# Set the number of clicks and the delay between each click
clicks = 32
delay = 1

# global x1, y1, x2, y2

x1 = 1886
y1 = 611
x2 = 1881
y2 = 500


def GetCurrentCoordinates():
    # Constants for left and right mouse buttons
    VK_LBUTTON = 0x01
    # VK_RBUTTON = 0x02

    while True:
        if win32api.GetAsyncKeyState(VK_LBUTTON) < 0:
            print("Left mouse button is clicked!")
            pyautogui.click()
            x1, y1 = pyautogui.position()
            print(f"Current Mouse Position: x1={x1}, y1={y1}")
            # time.sleep(delay+1)
            while True:
                if win32api.GetAsyncKeyState(VK_LBUTTON) < 0:
                    print("Left mouse button is clicked!")
                    pyautogui.click()
                    x2, y2 = pyautogui.position()
                    print(f"Current Mouse Position: x2={x2}, y2={y2}")
                    break
            break


# GetCurrentCoordinates()

flag = False
while True:
    if x1 is not None and y1 is not None:
        for i in range(clicks):
            if keyboard.is_pressed('esc'):
                flag = True
                print("Escape key pressed during clicks at position 1.")
                break
            pyautogui.click(x1, y1)
            time.sleep(delay)

        if flag:
            break

        for i in range(clicks):
            if keyboard.is_pressed('esc'):
                flag = True
                print("Escape key pressed during clicks at position 2.")
                break
            pyautogui.click(x2, y2)
            time.sleep(delay)

        if flag:
            break
