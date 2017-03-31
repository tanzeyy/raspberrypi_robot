import cv2
import numpy as np


def Capture(cap_src):

    cap = cv2.VideoCapture(cap_src)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 720)

    for i in xrange(10):
        cap.read()

    w = (0, 213)
    h = (0, 720)
    ret, frame = cap.read()
    img = frame[h[0]:h[1], w[0]:w[1]]
    cv2.imwrite('images/main.jpg', frame)
    cv2.imshow("frame", frame)
    cv2.imshow("img", img)

    cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()

Capture(0)
