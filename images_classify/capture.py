#!/usr/bin/env python

import cv2
import numpy as np
import os
import time

# Set the block pixel size
upper = [360, 760]
lower = [680, 1080]
width = 640
w = [0, width]
blocks = {
    "6": (w, lower), "5": (w, upper),
    "4": ([i+width for i in w], lower),
    "3": ([i+width for i in w], upper),
    "2": ([i+width*2 for i in w], lower),
    "1": ([i+width*2 for i in w], upper),
}


def Capture(shelf, side, cap_src=0):

    cap = cv2.VideoCapture(cap_src)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 1080)

    if not os.path.exists('images_classify/images/%s/%s' % (shelf, side)):
        os.makedirs('images_classify/images/%s/%s' % (shelf, side))

    var = 0

    for i in range(30):
        ret, frame = cap.read()
        frameVar = cv2.Laplacian(frame, cv2.CV_64F).var()
        if frameVar > var:
            proc_img = frame
            var = frameVar

    for block, area in blocks.items():
        img = proc_img[area[1][0]:area[1][1], area[0][0]:area[0][1]]
        if side == "left":
            block = str(int(block) + 6)
        cv2.imwrite(("images_classify/images/%s/%s/%s%s" + ".jpg") %
                    (shelf, side, shelf, block), img)
    cv2.imwrite('images_classify/images/%s/main.jpg' % shelf, proc_img)

    cap.release()
