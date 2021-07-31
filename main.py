import cv2
import numpy as np
import pyautogui
import time
from pynput.mouse import Button, Controller
from random import uniform

mouse = Controller()
# Fish Icon
fish_img = cv2.imread("fishicon.PNG", cv2.IMREAD_UNCHANGED)
fish_img = cv2.cvtColor(fish_img, cv2.COLOR_RGB2GRAY)
# Reel Green Icon
reel_img = cv2.imread("reel.PNG", cv2.IMREAD_UNCHANGED)
reel_img = cv2.cvtColor(reel_img, cv2.COLOR_RGB2GRAY)

w =  fish_img.shape[1]
h =  fish_img.shape[0]


def takeScreenshot():
    screenshot = pyautogui.screenshot(region=(700, 300, 400, 500))
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    return screenshot

def cast_bait():
    time.sleep(uniform(3, 4))
    mouse.press(Button.left)
    time.sleep(uniform(1.3, 1.8))
    mouse.release(Button.left)
    time.sleep(0.1)

def catch_fish():
    while True:
        screenshot = takeScreenshot()
        result = cv2.matchTemplate(screenshot, fish_img, cv2.TM_CCOEFF_NORMED)
        cv2.imshow("game", screenshot)
        
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        print(max_val)

        if max_val > 0.48:
            mouse.press(Button.left)
            time.sleep(0.05)
            mouse.release(Button.left)
            time.sleep(0.05)
            break
        cv2.waitKey(1)
    

        
def reel():
    i = 0
    while True:
        screenshot = takeScreenshot()
        result = cv2.matchTemplate(screenshot, reel_img, cv2.TM_CCORR_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        print(max_val)
        cv2.imshow("game", screenshot)

        if max_val > 0.80:
            i = 0
            mouse.press(Button.left)
            time.sleep(uniform(0.25, 0.35))
            mouse.release(Button.left)
            time.sleep(uniform(0.15, 0.25))
        else:
            i += 1
            if (i > 100):
                print("didnt find any reel icon")
                break
        cv2.imshow("game", screenshot)
        cv2.waitKey(1)

while True:
    cast_bait()
    catch_fish()
    reel()
    

    
  

