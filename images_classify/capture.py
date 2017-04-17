import cv2
import numpy as np
import os
import time

# Set the block pixel size
upper = [180, 648]
lower = [648, 1080]
width = 640
w = [0, width]
blocks = {
    "6": (w, lower), "5": (w, upper),
    "4": ([i+width for i in w], lower),
    "3": ([i+width for i in w], upper),
    "2": ([i+width*2 for i in w], lower),
    "1": ([i+width*2 for i in w], upper),
}


def Capture(shelf, side, cap_src=1):

    cap = cv2.VideoCapture(cap_src)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 1080)

    if not os.path.exists('images_classify/images/%s/%s' % (shelf, side)):
        os.makedirs('images_classify/images/%s/%s' % (shelf, side))

    for i in range(15):
        cap.read()
    # time.sleep(1.5)
    ret, frame = cap.read()
    for block, area in blocks.items():
        img = frame[area[1][0]:area[1][1], area[0][0]:area[0][1]]
        if side == "left":
            block = str(int(block) + 6)
        cv2.imwrite(("images_classify/images/%s/%s/%s%s" + ".jpg") %
                    (shelf, side, shelf, block), img)
    cv2.imwrite('images_classify/images/main.jpg', frame)

    cap.release()


