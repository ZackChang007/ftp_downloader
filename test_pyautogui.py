import pyautogui

screenWidth, screenHeight = pyautogui.size()  # Get the size of the primary monitor.
print(screenWidth, screenHeight)

currentMouseX, currentMouseY = pyautogui.position()  # Get the XY position of the mouse.
print(currentMouseX, currentMouseY)

# pyautogui.screenshot('test.png')
print(list(pyautogui.locateAllOnScreen('test.png')))


if __name__ == "__main__":
    print(1)

