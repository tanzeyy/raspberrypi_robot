#!/usr/bin/env python


# Python 2/3 compatibility
from __future__ import print_function

import RPi.GPIO as GPIO
import time


class Move(object):
    def __init__(self):
        self.cha1 = 29
        self.cha2 = 31
        self.red_enable = 33
        self.run_enable = 35
        self.loc_inp = 37
        self.speed_ctrl = 38

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

    def move_by_grid(self, distance):
        GPIO.output(self.run_enable, 1)
        GPIO.output(self.red_enable, 1)
        time.sleep(0.5)
        while True:
            try:
                # Waiting for the edge of loc_inp to record distance
                GPIO.wait_for_edge(self.loc_inp, GPIO.BOTH, timeout=5000)
                inp = GPIO.input(self.loc_inp)
                if inp == 0:
                    distance -= 1
                    print("Distance: ", distance)
                    if distance == 0:
                        self.stop()
                        break
                    time.sleep(0.4)
            except KeyboardInterrupt:
                self.stop()
            except:
                self.stop()

    def move_by_time(self, t):
        GPIO.output(self.run_enable, 1)
        GPIO.output(self.red_enable, 1)
        try:
            time.sleep(t)
            self.stop()
        except:
            self.stop()

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

    def set_speed(self, speed):
        if speed == 'fast':
            GPIO.output(self.speed_ctrl, 0)
        elif speed == 'slow':
            GPIO.output(self.speed_ctrl, 1)
        else:
            raise Exception("Speed input error!")

    def stop(self):
        GPIO.output(self.run_enable, GPIO.LOW)
        GPIO.output(self.red_enable, GPIO.LOW)
