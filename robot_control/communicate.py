import serial
import pickle

# Open port to send message to Arduino and PC
arm = serial.Serial("/dev/ttyACM0", 9600)
pc = serial.Serial("/dev/ttyUSB0", 9600)


def send2arm(msg):
    arm.write(msg)


def send2pc(msg):
    pc.write(msg)


def getResults():
    results = ""

    # Recive results by character
    while True:
        x = pc.read(1)

        # After recived '$' end character, stop reciving
        if x != '$':
            results += x
        else:
            break
    print(results)
    results = pickle.loads(results)
    # print res
    # print type(res)
    return results
