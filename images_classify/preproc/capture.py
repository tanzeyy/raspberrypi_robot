import cv2
import numpy as np

upper = [0, 360]
lower = [360, 720]
width = 213
w = [0, width]
blocks = {
    "12": (w, lower),
    "11": (w, upper),
    "10": ([i+width for i in w], lower),
    "9": ([i+width for i in w], upper),
    "8": ([i+width*2 for i in w], lower),
    "7": ([i+width*2 for i in w], upper),
    "6": ([i+width*3 for i in w], lower),
    "5": ([i+width*3 for i in w], upper),
    "4": ([i+width*4 for i in w], lower),
    "3": ([i+width*4 for i in w], upper),
    "2": ([i+width*5 for i in w], lower),
    "1": ([i+width*5 for i in w], upper)
}


def Capture(cap_src):

    cap = cv2.VideoCapture(cap_src)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 720)
    for i in xrange(10):
        cap.read()

    ret, frame = cap.read()
    for block in blocks:
        img = frame[blocks[block][1][0]:blocks[block][1][1],
                    blocks[block][0][0]:blocks[block][0][1]]
        cv2.imwrite("images_classify/images/"+str(block)+".jpg", img)
    cv2.imwrite('images_classify/images/test.jpg', frame)

    cap.release()
    cv2.destroyAllWindows()

Capture(0)
