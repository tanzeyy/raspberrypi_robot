import serial


class Grab(object):
    def __init__(self, position='upper', obj='jdb'):
        self.position = position
        self.obj = obj
