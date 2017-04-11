import serial
import time

# arm = "/dev/tty"
# car = "/dev/tty"


class Arm(object):
    def __init__(self, arm="/dev/tty"):
        self.arm = arm

    def send(self, msg, port=arm):
        ser = serial.Serial(port, 9600)
        ser.write(msg)

    def PreAction(self, position):
        send(position.encode('ascii'))

    def Grab(self, obj):
        send(obj.encode('ascii'))

    def Place(self, obj):
        send(obj.encode('ascii'))
