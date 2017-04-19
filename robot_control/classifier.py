#!/usr/bin/env python

import serial
import pickle


class Classifier(object):
    def __init__(self):
        self.pc_port = serial.Serial('/dev/ttyUSB0', 9600)

    def __del__(self):
        self.pc_port.close()

    def get_classify_results(self, shelf, side):
        results = ""

        # Send message to pc
        self.pc_port.write('capture')
        self.pc_port.write(shelf)
        self.pc_port.write(side)

        # Wait for results
        while True:
            # Recive results by character
            ch = pc_port.read(1)
            # After recived '$' end character, stop reciving
            if x != '$':
                results += x
            else:
                break
        results = pickle.loads(results)
        print(results)
        return results
