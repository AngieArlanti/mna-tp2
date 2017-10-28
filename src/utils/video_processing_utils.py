import cv2
import numpy as np
from math import pow, floor, log2
from enum import Enum
import os
import re

from src.passband_filter import PBFilter

RES_DIRECTORY = '../../res/videos/'

class Location(Enum):
    CENTER = 1
    LEFT = 2
    RIGHT = 3
    UPPER_CENTER = 4
    UPPER_LEFT = 5
    UPPER_RIGHT = 6
    LOWER_CENTER = 7
    LOWER_LEFT = 8
    LOWER_RIGHT = 9

class LedPreference(Enum):
    LED = 1
    NO_LED = 2
    BOTH = 3


def getFilteredRGBVectors(videoName, location, squareSize, timeLimit):
    cap = cv2.VideoCapture(videoName)

    if not cap.isOpened():
        print("No se pudo abrir el video.")
        return

    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    frameLimit = (int)(timeLimit * fps)
    if frameLimit > length:
        frameLimit = length

    n = int(pow(2, floor(log2(frameLimit))))

    [r, g, b] = calculateRGBMean(cap, location, frameLimit, squareSize)

    r = r[0, 0:n] - np.mean(r[0, 0:n])
    g = g[0, 0:n] - np.mean(g[0, 0:n])
    b = b[0, 0:n] - np.mean(b[0, 0:n])

    r_filtered = PBFilter().filter(r, fps)
    g_filtered = PBFilter().filter(g, fps)
    b_filtered = PBFilter().filter(b, fps)

    f = np.linspace(-n / 2, n / 2 - 1, n) * fps / n

    return [r_filtered, g_filtered, b_filtered, f]

    # Given a vector of frames it returns a vector for r, g and b bands with the mean calculated
    # in a square of squareSize located in location


def calculateRGBMean(cap, location, frameLimit, squareSize):
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # If the squareSize exceeds the max between width and height set a default
    if squareSize > max(width, height):
        squareSize = 30

    r = np.zeros((1, frameLimit))
    g = np.zeros((1, frameLimit))
    b = np.zeros((1, frameLimit))
    k = 0

    [leftBound, rightBound, upperBound, lowerBound] = calculateSquareBounds(location, width, height, squareSize)

    while (cap.isOpened() and k < frameLimit):
        ret, frame = cap.read()

        if ret == True:
            r[0, k] = np.mean(frame[leftBound:rightBound, upperBound:lowerBound, 0])
            g[0, k] = np.mean(frame[leftBound:rightBound, upperBound:lowerBound, 1])
            b[0, k] = np.mean(frame[leftBound:rightBound, upperBound:lowerBound, 2])
        # print(k)
        else:
            break
        k = k + 1

    cap.release()
    cv2.destroyAllWindows()
    return [r, g, b]


# Return [leftBound,rightBound,upperBound,LowerBound] of the square in which we are going to calculate the mean
# Default location is centered
def calculateSquareBounds(Location, width, height, squareSize):
    center = [int(width / 2 - squareSize / 2), int(width / 2 + squareSize / 2), int(height / 2 - squareSize / 2),
              int(height / 2 + squareSize / 2)]
    left = [0, squareSize, int(height / 2 - squareSize / 2), int(height / 2 + squareSize / 2)]
    right = [width - squareSize, width, int(height / 2 - squareSize / 2), int(height / 2 + squareSize / 2)]

    upperCenter = [int(width / 2 - squareSize / 2), int(width / 2 + squareSize / 2), 0, squareSize]
    upperLeft = [0, squareSize, 0, squareSize]
    upperRight = [width - squareSize, width, 0, squareSize]

    lowerCenter = [int(width / 2 - squareSize / 2), int(width / 2 + squareSize / 2), height - squareSize, height]
    lowerLeft = [0, squareSize, height - squareSize, height]
    lowerRight = [width - squareSize, width, height - squareSize, height]

    choices = {Location.CENTER: center, Location.LEFT: left, Location.RIGHT: right, Location.UPPER_CENTER: upperCenter,
               Location.UPPER_LEFT: upperLeft, Location.UPPER_RIGHT: upperRight, Location.LOWER_CENTER: lowerCenter,
               Location.LOWER_LEFT: lowerLeft, Location.LOWER_RIGHT: lowerRight}
    return choices.get(Location)


def getValidFileNames():
    validNames = []
    fileNames = os.listdir(RES_DIRECTORY)
    for name in fileNames:
        if not validateFileNameFormat(name) is None:
            validNames.append(name)
    return validNames


def getResourcesFromDirectory():
    fileNames = getValidFileNames()
    parsed = []
    for name in fileNames:
        noExtension = os.path.splitext(name)[0]
        parsed.append(noExtension.split('-', 2))
    return parsed


def validateFileNameFormat(name):
    pattern = re.compile("^[0-9]{2,3}\-(led|sinled)\-[a-zA-Z]+\.mp4$")
    return pattern.match(name)


def get_no_led_videos():
    no_leds = []

    for v in getResourcesFromDirectory():

        if v[1] == 'sinled':
            no_leds.append(v)

    return no_leds


def get_led_videos():
    leds = []

    for v in getResourcesFromDirectory():

        if v[1] == 'led':
            leds.append(v)

    return leds

def getFitbitHeartRates(LedPreference):
    fitbitHeartrates = []
    for resource in getResourcesFromDirectory():
        if((LedPreference == LedPreference.LED and resource[1]=='led')or(LedPreference == LedPreference.NO_LED and resource[1]=='sinled')or(LedPreference == LedPreference.BOTH)):
            fitbitHeartrates.append((int)(resource[0]))
    return fitbitHeartrates


# [r,g,b,f]=processVideo('71.mp4',Location.CENTER,30);
# print(r)
def testCalculateSquareBounds():
    print('----------------------------------------------------------------------------------------------')
    print(calculateSquareBounds(Location.CENTER, 720, 1280, 30))
    print(calculateSquareBounds(Location.LEFT, 720, 1280, 30))
    print(calculateSquareBounds(Location.RIGHT, 720, 1280, 30))
    print(calculateSquareBounds(Location.UPPER_CENTER, 720, 1280, 30))
    print(calculateSquareBounds(Location.UPPER_LEFT, 720, 1280, 30))
    print(calculateSquareBounds(Location.UPPER_RIGHT, 720, 1280, 30))
    print(calculateSquareBounds(Location.LOWER_CENTER, 720, 1280, 30))
    print(calculateSquareBounds(Location.LOWER_LEFT, 720, 1280, 30))
    print(calculateSquareBounds(Location.LOWER_RIGHT, 720, 1280, 30))
