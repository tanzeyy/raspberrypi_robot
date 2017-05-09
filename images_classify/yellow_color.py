#!/usr/bin/env python

import cv2
import numpy as np
import os


def is_yellow():
    images = os.listdir("images/A/")
    results = {}

    # Define range of yellow color in HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([130, 255, 255])

    for image in images:
        img = cv2.imread(str("images/A/" + image))
        # Convert BGR to HSV and threshold the image to get only yellow colors
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

        # Calculate the number of yellow pixels
        pixel_num = 0
        for item in mask:
            for i in item:
                pixel_num += i

        results[str(image).strip('.jpg')] = pixel_num

    # Pop the six elements with the smallest number of yellow pixels in results
    for i in range(6):
        results.pop(min(results.items(), key=lambda x: x[1])[0])

    for key, value in results.items():
        results[key] = 'yellow cube'

    return results
