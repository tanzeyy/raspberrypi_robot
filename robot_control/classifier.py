#!/usr/bin/env python

import serial
import pickle


class Classifier(object):
    def __init__(self):
        self.pc_port = serial.Serial('/dev/ttyUSB0', 9600)

    def __del__(self):
        self.pc_port.close()

    def get_classify_results(self):
        results = ""

        # Wait for results
        while True:
            # Recive results by character
            ch = self.pc_port.read(1)
            # After recived '$' end character, stop reciving
            if ch != '$':
                results += ch
            else:
                break

        return pickle.loads(results)

    def capture(self, shelf, side):
        self.pc_port.write('#')
        self.pc_port.write(shelf)
        self.pc_port.write(side)
        while True:
            ch = self.pc_port.read(1)
            if ch == '!':
                results = {}
                break
            elif ch == '~':
                results = get_classify_results()
                break
        return results
