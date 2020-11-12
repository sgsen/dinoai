from PIL import ImageGrab, ImageOps
# import tkinter as tk
import pyautogui
import time
import numpy as np
import mss
import cv2

# http://www.trex-game.skipser.com/


class Coords():
    replayButton = (400, 400)
    dinoLoc = (166, 405)
    floor_height = 438
    scan_ahead = 30
    scan_width = 50
    scan_height = 36
    scanZone1 = (176, 398, 200, 438)
    scanZone = {"top": 380, "left": 167, "width": 100, "height": 100}


def restartGame():
    pyautogui.click(Coords.replayButton)


def jumpDino():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')


def duckDino():
    pyautogui.keyDown('down')
    time.sleep(0.05)
    print("Duck")
    pyautogui.keyUp('down')


def scanAhead1():
    # 50 x 30 pixel scan zone
    # print(Coords.scanZone)
    img = ImageGrab.grab(Coords.scanZone)
    gImage = ImageOps.grayscale(img)
    imgColor = np.array(gImage.getcolors())
    imgColorSum = imgColor.sum()
    return gImage, imgColorSum


def scanAhead(sct):
    # 50 x 30 pixel scan zone
    # print(Coords.scanZone)
    img = np.array(sct.grab(Coords.scanZone))
    gImage = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    # imgColor = np.array(gImage.getcolors())
    imgColorSum = gImage.sum()
    return gImage, imgColorSum


restartGame()

with mss.mss() as sct:
    while "screen capturing":
        img = np.array(sct.grab(Coords.scanZone))
        gImage = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        cv2.imshow('OpenCV/Numpy grayscale', gImage)
        csum = gImage.sum()
        print(csum)
        if(csum < 2425000):
            jumpDino()
        time.sleep(0.1)  # pause for a bit..
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break


'''
attempt 2 with mss
with mss.mss() as sct:
    while "screen capturing":
        img = np.array(sct.grab(Coords.monitor))
        cv2.imshow('OpenCV/Numpy grayscale',
                   cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
'''


'''
# scan ahead attempt 1
#for i in np.arange(0, 100):
i = 0
while True:
    gimg, csum = scanAhead()
    print(i, csum)
    i +=1
    if(csum > 1207):
        #gimg.show()
        jumpDino()
        time.sleep(0.1)
        #gimg.close()

'''

'''
# intial test
# time.sleep(1)
# jumpDino()
# time.sleep(1)
# duckDino()
# time.sleep(1)
# duckDino()
# time.sleep(1)
# jumpDino()
'''
