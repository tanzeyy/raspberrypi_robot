import serial


def sendResults(shelf):
    # Open a port to send results
    port = serial.Serial("/dev/ttyUSB0", 9600)
    with open("images_classify/results/%s.txt" % shelf, 'r+') as fh:
        while True:
            result = fh.readline()
            if len(result) == 0:
                break
            port.write(result)

    fh.close()
    # Send the end character
    port.write('$')

# sendResults('A')
