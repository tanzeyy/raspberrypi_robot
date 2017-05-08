#!/usr/bin/env python

from __future__ import print_function
from classify import image_classify

import cv2
import numpy as np
import time
import serial


port = serial.Serial('/dev/ttyUSB0', 9600)
port.reset_input_buffer()

send_data_end_char = '$'
# classify_end_char = '~'.encode('utf-8')
# not_classify_end_char = '!'.encode('utf-8')

if not os.path.exists('images/A'):
        os.makedirs('images/A')

if not os.path.exists('images/BCD'):
        os.makedirs('images/BCD')


def send_results():
    with open("results.txt", 'r+') as fh:
        while True:
            result = fh.readline()
            if len(result) == 0:
                break
            port.write(result)

    fh.close()
    # Send the end character
    port.write(send_data_end_char)

block = ['2', '1', '3', '4', '6', '5', '7', '8', '10', '9', '11', '12']


def run(cap_src):

    num = 0

    cap = cv2.VideoCapture(cap_src)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 1080)

    while True:
        rcv = port.read(1)
        print('Recived: ' + rcv)

        if rcv == '#':
            shelf = port.read(1)
            if shelf == 'A':
                folder = 'A'
            else:
                folder = 'BCD'

            time.sleep(0.5)

            var = 0
            for i in range(15):
                ret, frame = cap.read()
                frame_var = cv2.Laplacian(frame, cv2.CV_64F).var()
                if frame_var > var:
                    image = frame
                    var = frame_var

            cv2.imwrite('images/%s/%s%s.jpg' %
                        (folder, shelf, block[num]), image)
            print('%s%s.jpg' % (shelf, block[num]), 'saved')

            num += 1
            if num == 11:
                num = 0
            port.write('!')
        elif rcv == '~':
            shelf = port.read(1)
            image_classify(shelf)
            send_results()


if __name__ == '__main__':
    run(1)
