import cv2
import numpy as np
import os

upper = [0, 240]
lower = [240, 480]
width = 206
w = [0, width]
blocks = {
    "6": (w, lower), "5": (w, upper),
    "4": ([i+width for i in w], lower),
    "3": ([i+width for i in w], upper),
    "2": ([i+width*2 for i in w], lower),
    "1": ([i+width*2 for i in w], upper),
}


def Capture(shelf, side, cap_src):

    cap = cv2.VideoCapture(cap_src)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
    if not os.path.exists('images_classify/images/%s' % shelf):
        os.makedirs('images_classify/images/%s' % shelf)

    for i in xrange(10):
        cap.read()

    ret, frame = cap.read()
    for block, area in blocks.items():
        img = frame[area[1][0]:area[1][1], area[0][0]:area[0][1]]
        if side == "left":
            block = str(int(block) + 6)
        cv2.imwrite(("images_classify/images/%s/%s%s" + ".jpg") %
                    (shelf, shelf, block), img)
    cv2.imwrite('images_classify/images/test.jpg', frame)

    cap.release()
    cv2.destroyAllWindows()

# Capture("A", "right", 1)
# Capture("A", "left", 0)
