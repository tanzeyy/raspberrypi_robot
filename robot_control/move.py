import RPi.GPIO as GPIO
import threading
import time


class Move(object):

    def __init__(self, dirc='up', distance=0,
                 loc_inp=7, channel=11, cha1=13, cha2=15):
        self.dirc = dirc
        self.distance = distance
        self.channel = channel
        self.cha1 = cha1
        self.cha2 = cha2
        self.loc_inp = loc_inp

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.loc_inp, GPIO.IN)
        GPIO.setup(self.channel, GPIO.OUT)
        GPIO.setup(self.cha1, GPIO.OUT)
        GPIO.setup(self.cha2, GPIO.OUT)

    def move(self, distance):
        GPIO.output(self.channel, GPIO.LOW)
        GPIO.output(self.channel, GPIO.HIGH)
        inp = GPIO.input(self.loc_inp)
        while inp == 0:
            time.sleep(1.5)
            distance = distance - 1
            print(distance)
            if distance == 0:
                GPIO.output(self.channel, GPIO.LOW)
                break

    def setDirection(self, dirc):
        if dirc == 'left':
            GPIO.output(self.cha1, 0)
            GPIO.output(self.cha2, 0)
        if dirc == 'right':
            GPIO.output(self.cha1, 0)
            GPIO.output(self.cha2, 1)
        if dirc == 'up':
            GPIO.output(self.cha1, 1)
            GPIO.output(self.cha2, 0)
        if dirc == 'down':
            GPIO.output(self.cha1, 1)
            GPIO.output(self.cha2, 1)

    def run(self, dirc, distance):
        self.setDirection(dirc)
        self.move(distance)

    def clean(self):
        GPIO.cleanup()

go = Move()
go.run('left', 3)
go.clean()
