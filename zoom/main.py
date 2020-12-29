import pyautogui
import subprocess
import time
def main():
    subprocess.call("C:/Users/mashh/AppData/Roaming/Zoom/bin/Zoom.exe")
    joinButton = pyautogui.locateCenterOnScreen("join_button.png")
    #time.sleep(4)
    pyautogui.moveTo(joinButton)
    pyautogui.click()

if __name__ == '__main__':
    main()