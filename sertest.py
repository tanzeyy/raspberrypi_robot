import serial
import classify
import send_results as sr

port = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)

while True:
    rcv = port.read(7)
    print("Reciving:" + rcv)
    if rcv == "capture":
        shelf = port.read(1)
        side = port.read(5)
        classify.run(shelf, side)
        sr.sendResults(shelf)

