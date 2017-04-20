#!/usr/bin/env python

import RPi.GPIO as GPIO
import time


class Mov(object):
    def __init__(self, dirc='up', distance=0, cha1=29, cha2=31,
                 red_enable=33, run_enable=35, loc_inp=37):
        self.dirc = dirc
        self.distance = distance
        self.cha1 = cha1
        self.cha2 = cha2
        self.red_enable = red_enable
        self.run_enable = run_enable
        self.loc_inp = loc_inp

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.cha1, GPIO.OUT)
        GPIO.setup(self.cha2, GPIO.OUT)
        GPIO.setup(self.red_enable, GPIO.OUT)
        GPIO.setup(self.run_enable, GPIO.OUT)
        GPIO.setup(self.loc_inp, GPIO.IN)

    def move(self, distance):
        GPIO.output(self.run_enable, GPIO.LOW)
        GPIO.output(self.red_enable, GPIO.LOW)
        GPIO.output(self.run_enable, GPIO.HIGH)
        GPIO.output(self.red_enable, GPIO.HIGH)
        try:
            time.sleep(0.5)
            while 1:
                GPIO.wait_for_edge(self.loc_inp, GPIO.BOTH, timeout=5000)
                inp = GPIO.input(self.loc_inp)
                if inp == 0:
                    distance -= 1
                    print(distance)
                    if distance == 0:
                        self.stop()
                        break
                    time.sleep(1)
        except:
            self.stop()

    def moveByTime(self, dirc, t):
        if dirc == 'no':
            self.stop()
        else:
            self.setDirection(dirc)
            GPIO.output(self.red_enable, 1)
            GPIO.output(self.run_enable, 1)
            time.sleep(t)
            self.stop()

    def setDirection(self, dirc):
        if dirc == 'left':
            GPIO.output(self.cha1, 0)
            GPIO.output(self.cha2, 1)
        if dirc == 'right':
            GPIO.output(self.cha1, 1)
            GPIO.output(self.cha2, 1)
        if dirc == 'up':
            GPIO.output(self.cha1, 1)
            GPIO.output(self.cha2, 0)
        if dirc == 'down':
            GPIO.output(self.cha1, 0)
            GPIO.output(self.cha2, 0)

    def run(self, dirc, distance):
        try:
            self.setDirection(dirc)
            self.move(distance)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        print("stop!")
        GPIO.output(self.run_enable, GPIO.LOW)
        GPIO.output(self.red_enable, GPIO.LOW)
        print("stop over!")

    def clean(self):
        print("clean")
        GPIO.cleanup()
        print("c over")


class Move(Mov):
    def __init__(self, speed_ctrl=40):
        self.speed_ctrl = speed_ctrl

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.speed_ctrl, GPIO.OUT)

    def set_speed(self, speed='fast'):
        if speed == 'fast':
            GPIO.output(self.speed_ctrl, 1)
        if speed == 'slow':
            GPIO.output(self.speed_ctrl, 0)

    def slow_run(self, dirc, distance):
        self.set_speed('slow')
        self.run(dirc, distance)

    def fast_run(self, dirc, distance):
        self.set_speed('fast')
        self.run(dirc, distance)

    def move_in_block(self, dirc):
        self.set_speed('slow')
        self.setDirection(dirc)
        self.moveByTime(2)


def init(go):
    go.run('right', 1)
