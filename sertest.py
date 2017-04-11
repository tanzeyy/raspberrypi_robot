import serial
import json
import classify

port = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)

while True:
    rcv = port.read(10)
    print("Reciving:" + rcv)
    if rcv == "capture":
        shelf = "A"
        classify.run('A', 'right')
        with open(('images_classify/results/%s' + '.json') % shelf) as results:
            results = json.load(results)
            for position, result in results.items():
                msg = (position + ':' + result + ';').encode('ascii')
                port.write(msg)
