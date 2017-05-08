#!/usr/bin/env python

import serial
from classify import image_classify
from capture import capture_images

port = serial.Serial("/dev/ttyUSB0", 9600)
port.reset_input_buffer()

send_data_end_char = '$'.encode('utf-8')
classify_end_char = '~'.encode('utf-8')
not_classify_end_char = '!'.encode('utf-8')


def send_results():
    with open("results.txt", 'r+') as fh:
        while True:
            result = fh.readline()
            if len(result) == 0:
                break
            port.write(result.encode('utf-8'))

    fh.close()
    # Send the end character
    port.write(send_data_end_char)


def run():
    while True:
        rcv = port.read(1).decode('utf-8')
        print('Reciving:' + rcv)
        if rcv == '#':
            rcv_data = port.read(6).decode('utf-8')
            shelf = rcv_data[0]
            side = rcv_data[1:].strip()
            print(shelf, side)
            capture_images(shelf, side)
            if shelf == 'A' and side == 'left':
                image_classify(shelf)
                port.write(classify_end_char)
                send_results()
            elif shelf == 'D' and side == 'left':
                image_classify(shelf)
                port.write(classify_end_char)
                send_results()
            else:
                port.write(not_classify_end_char)


if __name__ == '__main__':
    run()
