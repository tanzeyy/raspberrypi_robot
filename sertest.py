import serial
import json
import test

port = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)

while True:
    rcv = port.read(10)
    print("Reciving:" + rcv)
    if rcv == "capture":
        test.run()
        with open('images_classify/results/results.json') as results:
            results = json.load(results)
            for position, result in results.items():
                msg = (position + ':' + result + ';').encode('ascii')
                port.write(msg)
