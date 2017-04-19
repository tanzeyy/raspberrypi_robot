#!/usr/bin/env python

import serial
import time


class Arm(object):
    def __init__(self):
        self.arm_port = serial.Serial('/dev/ttyACM0', 9600)

    def open_paw(self):
        self.arm_port.write('O')
        self.wait_for_act_end_signal()

    def grab(self, obj):
        self.arm_port.write(obj)
        self.wait_for_act_end_signal()

    def place(self):
        self.arm_port.write('P')
        self.arm_port.write('O')
        self.wait_for_act_end_signal()

    def restore(self):
        self.arm_port.write('R')
        self.wait_for_act_end_signal()

    def capture(self):
        self.arm_port.write('T')
        self.wait_for_act_end_signal()

    def act(self, act):
        self.arm_port.write(act)
        self.wait_for_act_end_signal()

    def rotate_to_shelf(self, shelf):
        if shelf == 'A':
            self.arm_port.write('d')
        elif shelf == 'B':
            self.arm_port.write('r')
        elif shelf == 'C':
            self.arm_port.write('u')
        elif shelf == 'D':
            self.arm_port.write('l')
        else:
            raise Exception('Shelf input error!')
        time.sleep(1)

    def rotate_to_cart(self, cart):
        if cart == '1':
            self.arm_port.write('u')
        elif cart == '2' or cart == '3' or cart == '4':
            self.arm_port.write('l')
        elif cart == '5' or cart == '6' or cart == '7':
            self.arm_port.write('d')
        elif cart == '8' or cart == '9' or cart == '10':
            self.arm_port.write('r')
        else:
            raise Exception('Cart number error!')
        time.sleep(1)

    def wait_for_act_end_signal(self):
        print("Waiting for end signal...")
        while True:
            sig = self.arm_port.read(2)
            if sig == 'ok':
                break
        print(sig)
        print("End signal recived! Continue running!")
