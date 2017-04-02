import cv2
import numpy as np
import os

upper = [0, 240]
lower = [240, 480]
w = [200, 400]
blocks = {
    "upper": (w, upper),
    "lower": (w, lower)
}


def Capture(cap_src):

    cap = cv2.VideoCapture(cap_src)
    # cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    # cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

    if not os.path.exists('images_classify/images'):
        os.makedirs('images_classify/images')

    for i in range(5):
        cap.read()

    ret, frame = cap.read()
    for block, area in blocks.items():
        img = frame[area[1][0]:area[1][1], area[0][0]:area[0][1]]
        cv2.imwrite(("images_classify/images/%s" + ".jpg") % block, img)
    # cv2.imwrite('images_classify/images/test.jpg', frame)

    cap.release()
    cv2.destroyAllWindows()

Capture(0)
