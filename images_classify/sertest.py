import serial
from classify import image_classify
from capture improt capture_images

port = serial.Serial("/dev/ttyUSB0", 9600, timeout=0.5)
port.reset_input_buffer()


def send_results():
    with open("results.txt", 'r+') as fh:
        while True:
            result = fh.readline()
            if len(result) == 0:
                break
            port.write(result)

    fh.close()
    # Send the end character
    port.write('$')


def run():
    while True:
        rcv = port.read(1)
        print("Reciving:" + rcv)
        if rcv == "#":
            shelf = port.read(1)
            side = port.read(5)
            capture_images(shelf, side)
            if shelf == 'A' and side == 'left':
                image_classify(shelf)
                port.write('~')
                send_results()
            elif shelf == 'D' and side == 'left':
                image_classify(shelf)
                port.write('~')
                send_results()
            else:
                port.write('!')
