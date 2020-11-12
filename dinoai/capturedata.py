import os
import time
import cv2
from mss import mss
import numpy as np
import keyboard
from dinoCoords import DinoGrab


'''
The basic idea here is to do the following:

While I am playing the game
1. Grab the game-play screen at some specific points:
when I jump or duck; and a few when I do nothing (hit 'd')
2. Process the screen grap to capture the edges only
3. Store the screen grab as well as the key stroke

guidance: https://github.com/jg-fisher/
dinoAI/blob/master/capture/capture_feed.py
game:
http://www.trex-game.skipser.com/
'''


# Helper function to process image
def processImage(img):
    # put into an array
    img = np.array(img)

    # resize the image
    img = cv2.resize(img, None, fx=0.5, fy=0.5)

    # convert to gray scale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # keep the edges
    img = cv2.Canny(img, threshold1=100, threshold2=200)

    return img


def keepImage(img, counter):
    img = processImage(img)
    print('write image')
    cv2.imwrite(f'{DinoGrab.datapath}/{DinoGrab.folderName}/frame_{counter}.jpg',
                img)
    return


# Until I quit, keep capturing the images based on key strokes
def recordDinoPlay():
    # screen grab context
    sct = mss()

    # set counter
    i = 0

    with open(f'{DinoGrab.datapath}/{DinoGrab.folderName}/actions.csv',
         'w') as csv:

        while "recording":
            # slow down the capture a bit
            time.sleep(0.1)
            # take screen grab
            img = sct.grab(DinoGrab.scrBox)

            if keyboard.is_pressed('up arrow'):
                keepImage(img, i)
                csv.write('1\n')
                print('dino jump')
                i += 1

            if keyboard.is_pressed('down arrow'):
                keepImage(img, i)
                csv.write('2\n')
                print('dino duck')
                i += 1

            if keyboard.is_pressed('d'):
                keepImage(img, i)
                csv.write('0\n')
                print('dino chill')
                i += 1

            # break the video feed
            if keyboard.is_pressed('q'):
                csv.close()
                # cv2.destroyAllWindows()
                break
    return


def main():
    # Prep where to store the images

    if not os.path.exists(f'{DinoGrab.datapath}/{DinoGrab.folderName}'):
        os.mkdir(f'{DinoGrab.datapath}/{DinoGrab.folderName}')

    # record game play
    recordDinoPlay()


if __name__ == "__main__":
    main()
