import cv2
import numpy as np


def IsYellow(image):

    # Number of yellow pixels
    pixel_num = 0

    # Hsv range of yellow color
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([130, 255, 255])

    # Threshold to be determined
    thr = 1000

    # Read image
    img = cv2.imread(image)
    # BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Filter out yellow pixels
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Calculate the number of yellow pixels
    for item in mask:
        for pixel in item:
            pixel_num += pixel

    # Compare with the threshold
    if pixel_num > thr:
        return 1


def FindYellowCube(images, func=IsYellow):
    results = {}
    for image in images:
        img = "images_classify/images/A/" + image
        if func(img) == 1:
            results[str(image).strip('.jpg')] = "yellow cube"
    return results
