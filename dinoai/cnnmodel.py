# imports
import os
import cv2
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from dinoCoords import DinoGrab


def loadGameData(path):
    # adjust path by adding fwd slash
    path = path+"/"

    # read in the data
    all_actions = []
    all_images = []

    # get the directory names
    gamefolders = []
    for f in os.listdir(path):
        if os.path.isdir(os.path.join(path, f)):
            gamefolders.append(f)

    print(f"Folders List: {gamefolders}")

    # read images and actions from the folders
    for folder in gamefolders:
        # #get all the files in this directory
        # print(folder)
        pathf = path+folder+"/"
        # print(pathf)

        # #read the variables from img files
        # how many images
        imgcount = len([name for name in os.listdir(pathf)
                        if os.path.isfile(os.path.join(pathf, name))])
        # ignore actions file and last 2 images which often have game over.
        # also note this is indexed from 1.
        imgcount = imgcount - 3
        # print(f"Image Count: {imgcount}")

        for i in range(imgcount):
            img = cv2.imread(pathf+f'frame_{i}.jpg', cv2.IMREAD_GRAYSCALE)
            # img = cv2.resize(img, None, fx=0.5, fy=0.5)
            all_images.append(img)

        # #deal with labels from action.csv
        actionslist = []
        with open(pathf+'actions.csv', 'r') as actions:
            for line in actions:
                actionslist.append(line.rstrip())
        # want to omit game over img actions
        all_actions = all_actions + actionslist[0:imgcount]

    # verify that it is working
    print(f"Total images loaded: {len(all_images)}")
    print(f"Total actions loaded: {len(all_actions)}")

    # store as arrays
    X = np.array(all_images)
    Y = np.array(all_actions)
    return X, Y


def trainModel(X, Y):
    # convolutions requires single tensor (4D list)
    X = X[..., np.newaxis]

    # images adimensions for input shape
    img_dims = X[0].shape

    # scale the input data
    X = X / np.max(X)

    # cnn can only recommend actions: jump, duck, and chill
    rec_actions = len(np.unique(Y))

    # convert Y from string to float
    Y = Y.astype(np.float)

    # split into training and test
    x_train, x_test, y_train, y_test = train_test_split(
        X, Y, test_size=.2, random_state=1)

    # model design
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (2, 2), activation='relu',
                               input_shape=img_dims),
        tf.keras.layers.MaxPool2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(rec_actions, activation='softmax')
    ])

    # compile the model
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    # fit the model
    model.fit(x_train, y_train, epochs=8)

    # model accuracy
    test_loss, test_acc = model.evaluate(x_test, y_test)
    print(test_acc)

    return model


def main():
    # load game data

    X, Y = loadGameData(DinoGrab.datapath)

    # train model
    trained_model = trainModel(X, Y)

    # save the model
    trained_model.save(DinoGrab.modelpath)

    return


if __name__ == "__main__":
    main()
