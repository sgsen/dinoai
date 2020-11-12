from datetime import datetime


class DinoGrab():
    # screen grab coordinates
    # set for asus zenbook laptop with http://www.trex-game.skipser.com/
    # on left half of screen
    scrBox = {
        "top": 362,
        "left": 185,  # avoid snout on duck
        "width": 300,  # how far to look ahead
        "height": 100  # avoid the ground
    }

    # location of the replay button
    replayButton = (400, 400)

    # model path
    modelpath = "./model/aidino"

    # data path for image storage
    datapath = "./capturedata"

    # folder for image storage
    folderName = datetime.now().strftime("%d%m%y%H%M%S")
