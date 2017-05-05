#!/usr/bin/env python


# Python 2/3 compatibility
from __future__ import print_function

import RPi.GPIO as GPIO
import time
import threading


class Move(object):
    def __init__(self):
        self.cha1 = 29
        self.cha2 = 31
        self.red_enable = 33
        self.run_enable = 35
        self.loc_inp = 37
        self.speed_ctrl = 38

        self.speed = 'slow'
        self.direction = 'right'

        # Set up channels

        # cha1 & cha2: set up the moving direction
        # red_enable: open the infrared trace
        # loc_inp: return signal of the distance
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.cha1, GPIO.OUT)
        GPIO.setup(self.cha2, GPIO.OUT)
        GPIO.setup(self.red_enable, GPIO.OUT)
        GPIO.setup(self.run_enable, GPIO.OUT)
        GPIO.setup(self.loc_inp, GPIO.IN)
        GPIO.setup(self.speed_ctrl, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def move_by_grid(self, distance):
        GPIO.output(self.run_enable, 1)
        GPIO.output(self.red_enable, 1)
        # Avoid detecting the start point
        time.sleep(0.5)
        if self.speed = 'fast':
            check_time = 1000
        else:
            check_time = 2100

        while True:
            # Waiting for the edge of loc_inp to record distance
            channel = GPIO.wait_for_edge(self.loc_inp, GPIO.BOTH,
                                         timeout=check_time)
            if channel is not None:
                if not GPIO.input(self.loc_inp):
                    distance -= 1
                    print("Distance: ", distance)
                    if distance == 0:
                        self.stop()
                        break
                    time.sleep(0.4)

            else:  # Detection timeout
                self.stop()
                break

        return distance

    def move_by_time(self, t):
        GPIO.output(self.run_enable, 1)
        GPIO.output(self.red_enable, 1)
        try:
            time.sleep(t)
            self.stop()
        except:
            self.stop()

        return 0

    def set_direction(self, dirc):
        if dirc == 'left':
            GPIO.output(self.cha1, 0)
            GPIO.output(self.cha2, 1)
        elif dirc == 'right':
            GPIO.output(self.cha1, 1)
            GPIO.output(self.cha2, 1)
        elif dirc == 'up':
            GPIO.output(self.cha1, 1)
            GPIO.output(self.cha2, 0)
        elif dirc == 'down':
            GPIO.output(self.cha1, 0)
            GPIO.output(self.cha2, 0)
        else:
            raise Exception("Direction input error!")
        self.direction = dirc

    def set_speed(self, spd):
        if spd == 'fast':
            GPIO.output(self.speed_ctrl, 1)
        elif spd == 'slow':
            GPIO.output(self.speed_ctrl, 0)
        else:
            raise Exception("Speed input error!")
        self.speed = spd

    def stop(self):
        GPIO.output(self.run_enable, GPIO.LOW)
        GPIO.output(self.red_enable, GPIO.LOW)
