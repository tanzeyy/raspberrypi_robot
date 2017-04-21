import serial
import classify
import send_results as sr

port = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
port.reset_input_buffer()

while True:
    port.flushInput()
    rcv = port.read(1)
    print("Reciving:" + rcv)
    if rcv == "#":
        port.reset_input_buffer()
        shelf = port.read(1)
        side = port.read(5)
        classify.run(shelf, side)
        sr.sendResults(shelf)

