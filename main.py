import sys

import pyautogui
import playsound
from PIL import ImageGrab
from PIL import Image
from screeninfo import get_monitors
from functools import partial
import time

def diffcheck(image, imgnum, tolerance):
    red, green, blue =image.getpixel((2, 2))
    img = str(imgnum) + ".png"
    red = float(red)
    green = float(green)
    blue = float(blue)
    #print(img)
    red1, green1, blue1, dontcare1 = Image.open(img).getpixel((2, 2))
    red1 = float(red1)
    green1 = float(green1)
    blue1 = float(blue1)
    #print(red, blue, green, red1, blue1, green1)
    if (100 + tolerance) > ((red / red1) * 100) > (100 - tolerance):
        if (100 + tolerance) > ((green / green1) * 100) > (100 - tolerance):
            if (100 + tolerance) > ((blue / blue1) * 100) > (100 - tolerance):
                return True
    return False

try:
    ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
    topleft = 0
    for m in get_monitors():
        if (topleft > m.x): topleft = m.x
    soundFile = './Cylen.wav'
    counter = 1
    print("Running")
    while True:
        happens = 0
        test = ""
        while True:
            #print("run")
            pyautogui.sleep(1)
            count=0
            test = pyautogui.locateOnScreen('1.png', confidence=0.99)
            if str(test) != "None":
                im = pyautogui.screenshot(region=[test.left, test.top, test.width, test.height])
                if diffcheck(im, 1, 40):
                    happens = 1
                    break
            test = pyautogui.locateOnScreen('2.png', confidence=0.99)
            if str(test) != "None":
                im = pyautogui.screenshot(region=[test.left, test.top, test.width, test.height])
                if diffcheck(im, 2, 40):
                    happens = 2
                    break
            test = pyautogui.locateOnScreen('3.png', confidence=0.99)
            if str(test) != "None":
                im = pyautogui.screenshot(region=[test.left, test.top, test.width, test.height])
                if diffcheck(im, 3, 40):
                    happens = 3
                    break
            test = pyautogui.locateOnScreen('4.png', confidence=0.99)
            if str(test) != "None":
                all = pyautogui.locateAllOnScreen('4.png',confidence=0.99)
                for im in all:
                    im = pyautogui.screenshot(region=[test.left, test.top, test.width, test.height])
                    if diffcheck(im, 4, 40):
                        happens = 4
                        break
                    if diffcheck(im, 5, 40):
                        happens = 5
                        break
                if happens !=0:
                    break
        if happens != 0:
            #print(test)
            #print(happens)
            #save = "./image" + str(counter) + ".png"
            #counter += 1
            #im.save(save)
            print("Detected")
            playsound.playsound(soundFile)
except Exception as e:
    crash=["Error on line {}".format(sys.exc_info()[-1].tb_lineno),"\n",e]
    print(crash)
    timeX = str(time.time())
    with open("CRASH-" + timeX + ".txt", "w") as crashLog:
        for i in crash:
            i = str(i)
            crashLog.write(i)
