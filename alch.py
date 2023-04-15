

import os


import matplotlib.pyplot as plt
import numpy as np

import cv2

import pyautogui
import time
import random
import math
from PIL import Image





# timebetweenclicks
TBCmean = .65
TBCvariance = 0.032
waitTillLilRestRand = random.randrange(130, 198)


def randomTBCtime():
    global TBCmean
    global TBCvariance
    global waitTillLilRestRand
    # print("tbcMean ", TBCmean)
    TBCmean += (random.random() - .5) / 140
    TBCvariance += (random.random() - .5) / 700
    if TBCvariance > .36:
        TBCvariance = 0.036
    if TBCvariance < .022:
        TBCvariance = .022
    if TBCmean > .65:
        TBCmean = 0.65
    if TBCmean < .55:
        TBCmean = .55
    # print(t)
    if random.randrange(0, 11) > 9:
        x = random.uniform(TBCmean - .07, TBCmean + .11)
    elif random.randrange(0, 15) > 13:
        x = random.uniform(.47, .77)
    elif random.randrange(0, 20) > 18:
        x = random.uniform(.43, .89)
    else:
        x = random.normalvariate(TBCmean, TBCvariance)
    if random.randrange(0, 201) > waitTillLilRestRand:
        waitTillLilRestRand = random.randrange(130, 198)
        return (x + random.random() * random.randrange(0, 3))
    return (x)


# def getText(img):
#     img = keras_ocr.tools.read(img)
#     # Prediction_groups is a list of (word, box) tuples
#     prediction_groups = pipeline.recognize([img])
#     # print image with annotation and boxes
#     # keras_ocr.tools.drawAnnotations(image=img, predictions=prediction_groups[0])
#     print(prediction_groups[0][0][0])
mdtimeMean = 0.1


def randomMDtime():
    global mdtimeMean
    # print("mdtMean ", mdtimeMean)
    mdtimeMean += (random.random() - .5) / 500
    if mdtimeMean > .11:
        mdtimeMean = 0.11
    if mdtimeMean < .084:
        mdtimeMean = .084
    if random.randrange(0, 20) > 17:
        x = random.uniform(mdtimeMean - 0.03, mdtimeMean + 0.03)
    elif random.randrange(0, 20) > 19:
        x = random.uniform(mdtimeMean - 0.04, mdtimeMean + 0.05)
    elif random.randrange(0, 20) > 18:
        x = random.uniform(.04, .15)
    else:
        x = random.normalvariate(mdtimeMean, .01)
    # print(x)
    return (x)

reactionTimeMean = 0.32
def reaction_time():
    global fatigue
    global reactionTimeMean
    # print("mdtMean ", mdtimeMean)
    reactionTimeMean += (random.random() - .5) / 500
    if reactionTimeMean > .39:
        reactionTimeMeann = 0.389
    if reactionTimeMean < .318:
        reactionTimeMean = .32
    if random.randrange(0, 20) > 17:
        x = random.uniform(reactionTimeMean - 0.01, reactionTimeMean + 0.03)
    elif random.randrange(0, 20) > 19:
        x = random.uniform(reactionTimeMean - 0.02, reactionTimeMean + 0.05)
    elif random.randrange(0, 20) > 18:
        x = random.uniform(.25, .38)
    else:
        x = random.normalvariate(reactionTimeMean, .01)
    # print(x)
    bonus_fatigue  = (fatigue*(random.random()/1000) - 0.02) *2 #0.03-0.05 ish? then ( - 0.02) * 2
    return (x+bonus_fatigue)







randomPersist = random.randrange(70, 99)



import time


font = cv2.FONT_HERSHEY_COMPLEX_SMALL






def check_Alch_state_inv_or_magic():
    #menuGrey min max
    # np.array([10 , 51, 48]), np.array([24 , 89, 79])
    min =np.array([10 , 51, 48])
    max = np.array([24 , 89, 79])
    #left  top width height
    im = pyautogui.screenshot(region=(1726,589,489,263))
    im = np.array(im)[:, :, :3]  # Get first 3 channel from image as numpy array.
    # cv2.imshow("im",im)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    #change image to correct colour space
    im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    # rMask = cv2.inRange(hsv, rMin, rMax)
    Mask = cv2.inRange(hsv, min, max)
    # cv2.imshow("im", im)
    # cv2.waitKey(0)
    #check percentage of the image that  is within this range
    print((Mask > 0).mean())
    if (Mask > 0).mean() > 0.87:
        return("inv")#inv
    else:
        return("magic")#magic





def handleSnooze():
    global fatigue
    print(fatigue)
    if fatigue > random.randrange(35,55):
        snooze_perhaps()
        fatigue -= random.randrange(8,16)

def snooze_perhaps():
    if random.randrange(0, 100) > 80:
        print("shortBreak")
        time.sleep(random.randrange(5, 20))
        time.sleep(randomMDtime() * random.random() * random.randrange(1, 5))
        snooze_perhaps()
    if random.randrange(0, 100) > 97:
        print("shortshortBreak")
        time.sleep(random.randrange(5, 10))
        time.sleep(randomMDtime() * random.random() * random.randrange(1, 5))
        snooze_perhaps()




from datetime import datetime

random.seed(datetime.now().timestamp())
lastClickAny = time.time()
init = 3  # we subtract this and use it to show ui at first? #3 rn
running = True
setup = True
invOpen = False
magicOpen = False
import winsound

winsound.Beep(440, 500)



mdtimeMean = 0.1
def randomMDtime():
    global mdtimeMean
    # print("mdtMean ", mdtimeMean)
    mdtimeMean += (random.random()-.5)/500
    if mdtimeMean > .11:
        mdtimeMean = 0.11
    if mdtimeMean < .084:
        mdtimeMean = .084
    if random.randrange(0,20) > 17:
        x = random.uniform(mdtimeMean - 0.03, mdtimeMean + 0.03)
    elif random.randrange(0,20) > 19:
        x = random.uniform(mdtimeMean - 0.04, mdtimeMean + 0.05)
    elif random.randrange(0,20) > 18:
        x = random.uniform(.04, .15)
    else:
        x = random.normalvariate(mdtimeMean, .01)
    # print(x)
    return(x)


setup = True
running = True



#function time example
functionTimer = time.time()
# function
runTime = time.time()-functionTimer


# #function time example
# functionTimer = time.time()
# # function
# runTime = time.time()-functionTimer
fatigue = 0
def alchBB(x,y):
    global fatigue
    running = True
    state = check_Alch_state_inv_or_magic()
    waiting = 0
    mouseDownTime = randomMDtime()
    pyautogui.mouseDown()
    time.sleep(mouseDownTime)
    pyautogui.mouseUp()
    time.sleep(randomTBCtime()*0.66)
    while running:
        screenState = check_Alch_state_inv_or_magic()
        if screenState != state:
            state = screenState
            time.sleep(reaction_time() + 0.02)
            xAct, yAct = pyautogui.position()
            if abs(xAct - x) > 20 or abs(yAct - y) > 20:
                print("pausing, hit enter to continue")
                input()
            mouseDownTime =  randomMDtime()
            pyautogui.mouseDown()
            time.sleep(mouseDownTime)
            pyautogui.mouseUp()
            time.sleep(randomTBCtime()*0.3)
            waiting = 0
            fatigue += 1
            handleSnooze()
        else:
            time.sleep(0.06)
            waiting += 1
            if waiting > 40:
                print("something wrong, pausing, hit enter to continue")
                winsound.Beep(340, 500)
                winsound.Beep(240, 500)
                input()


def main():
    winsound.Beep(440, 100)
    print("please move mouse to start location")
    time.sleep(2)
    winsound.Beep(440, 900)
    winsound.Beep(340, 500)
    mouseLocX, mouseLocY = pyautogui.position()
    time.sleep(1)
    xAct, yAct = pyautogui.position()
    if abs(xAct - mouseLocX) > 10 or abs(yAct - mouseLocY) > 10:
        print("pausing, hit enter to continue")
        input()
    alchBB(mouseLocX,mouseLocY)

    # global fatigue
    # x = []
    # for i in range(10000):
    #     x.append(reaction_time())
    #     fatigue += 1
    #     handleSnooze()
    # print("kk")
    # plt.hist(x, density=True, bins=90)  # density=False would make counts
    # plt.ylabel('Probability')
    # plt.xlabel('Data');
    # plt.show()
    # print("plotted")
    # input()



main()
