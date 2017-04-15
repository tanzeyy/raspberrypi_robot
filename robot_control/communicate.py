import serial
import json

arm = serial.Serial("/dev/ttyACM0", 9600)
pc = serial.Serial("/dev/ttyAMA0", 9600)


def send2arm(msg):
    arm.write(msg)


def send2pc(msg):
    pc.write(msg)


def getResults():
    L = 0
    while True:
        fh = open("results.json", 'r+')
        fh.seek(L)
        x = pc.read(1)
        if x != ' ':
            fh.write(x)
            L += 1
        fh.close()


def get():
    results = ""
    while True:
        x = pc.read(1)
        if x != ' ':
            results += x
        if x == '$':
            break
    print results
    print type(results)
    results = results[:-1]
    res = json.loads(results, encoding='unicode')
    print res
    print type(res)
