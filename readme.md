# Dino AI Project
Soham | Oct 29, 2020

Fun, canonical, project to explore the basics of a convolutional neural net for computer vision. The idea was to try to build a bot to play the [chrome dinosaur game][5], and that is what this code does.

I had lots of help. There are lots of guides on YouTube and elsewhere. Two in particular were the basis for me:

1. Rough [YouTube video][1] that gets you the general idea of how the basic set up to capture screenshots and deploy a bot.

2. A [github repo][2] that demonstrates how to structure a project to capture training data, build the CNN, and deploy the bot.

I didn't build the game from scratch. I use a ripped version (so I wouldn't have to wait for the internet to go out!) from [here][3]. I am also relying on an overview of [Tensorflow][4] from this Udemy Course.

The project has three parts:

1. Capture the training data in capturedata.py. This was mainly an exercise in getting to know the the OpenCV package.

2. Build the CNN in cnnmodel.py. I use TensorFlow here to build the CNN.

3. Deploy the bot in deploydinoai.py. Here I mainly use the pyautogui package.

Something I would like to try next is to build apply a genetic algorithm so the model can train itself, and spare me having to play endless hours of chrome dino.

[1]:https://www.youtube.com/watch?v=bf_UOFFaHiY
[2]:https://github.com/jg-fisher/dinoAI/
[3]:http://www.trex-game.skipser.com/
[4]:https://www.udemy.com/course/deep-learning-tensorflow-2/
[5]:https://en.wikipedia.org/wiki/Dinosaur_Game