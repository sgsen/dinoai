# from PIL import ImageGrab, ImageOps, Image
# import tkinter as tk
# import cv2
import pyautogui
import time
import numpy as np
from mss import mss
from tensorflow.keras.models import load_model
import capturedata as cd
from dinoCoords import DinoGrab


def jumpDino(msg="Jump"):
    pyautogui.press('space')
    print(msg)


def duckDino():
    pyautogui.press('down')
    print("Duck")


def startGame():
    pyautogui.click(DinoGrab.replayButton)
    jumpDino("Start")


def deployDino(sct, dinoBrain):
    # capture image: what's ahead of the dino?
    img = sct.grab(DinoGrab.scrBox)

    # process image
    img = cd.processImage(img)

    # use model to predict action
    # #make the 4D input the model expects
    img = img[np.newaxis, :, :, np.newaxis]

    # apply model
    action_rec = dinoBrain.predict(img)
    action_rec = action_rec.argmax(axis=-1)

    # execute action
    if action_rec == 1:
        jumpDino()
    elif action_rec == 2:
        duckDino()
    else:
        print("Chill")
        pass

    # pause for a short moment before going back
    time.sleep(.095)
    return


def main():
    # load the model
    dinoBrain = load_model(DinoGrab.modelpath)

    # start the game
    # you have to manually open up http://www.trex-game.skipser.com/
    startGame()

    # deploy the ai dino
    sct = mss()
    while "PlayingGame":
        deployDino(sct, dinoBrain)


if __name__ == "__main__":
    main()
