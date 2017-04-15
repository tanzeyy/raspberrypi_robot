import serial


def sendResults(shelf):
    port = serial.Serial("/dev/ttyUSB0", 9600)
    with open("results/%s.json" % shelf, 'r+') as fh:
        while True:
            result = fh.readline()
            if len(result) == 0:
                break
            port.write(result)

    fh.close()
    port.write('$')

sendResults('A')

