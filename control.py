import serial
ser = serial.Serial('COM26')  # open serial port Windows
#ser = serial.Serial('/dev/ttyUSB0')  # open serial port Linux / Mac
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()             # close port

lineaiz = 0
lineader = 0
STOP = 0
close = 0
home = 0
solicitud = 0
s1a = 0
s1b = 0
s2a = 0
s2b = 0

def leerQR():
    print("QR Read")

def enviarComando(comando):
    print(comando)

def ir1A ():
    print("forward")
    if lineaiz == 1:
        print("turn left")
        print('forward')
        if lineaiz == 1:
            print("turn right")
            print("forward")
            if STOP == 1:
                print("STOP")
                if close == 1:
                    print("180")
                    if home == 1:
                        print("forward")
                        if lineader == 1:
                            print("turn left")
                            print("forward")
                            if lineader == 1:
                                print("turn right")
                                print("forward")
                                if STOP == 1:
                                    print("STOP")
    return


def ir1B ():
    print("forward")
    if lineaiz == 1:
        print("turn left")
        print('forward')
        if lineader == 1:
            print("turn right")
            print("forward")
            if STOP == 1:
                print("STOP")
                if close == 1:
                    print("180")
                    if home == 1:
                        print("forward")
                        if lineaiz == 1:
                            print("turn left")
                            print("forward")
                            if lineader == 1:
                                print("turn right")
                                print("forward")
                                if STOP == 1:
                                    print("STOP")
    return

def ir2A ():
    print("forward")
    if lineader == 1:
        print("turn right")
        print("forward")
        if lineaiz == 1:
            print("turn left")
            print("forward")
            if STOP == 1:
                print("STOP")
                if close == 1:
                    print("180")
                    if home == 1:
                        print("forward")
                        if lineader == 1:
                            print ("turn right")
                            print ("forward")
                            if lineaiz == 1:
                                print ("turn left")
                                print ("forward")
                                if STOP == 1:
                                    print ("STOP")
    return

def ir2B ():
    print("forward")
    if lineader == 1:
        print("turn right")
        print('forward')
        if lineader == 1:
            print("turn left")
            print("forward")
            if STOP == 1:
                print("STOP")
                if close == 1:
                    print("180")
                    if home == 1:
                        print("forward")
                        if lineaiz == 1:
                            print("turn right")
                            print("forward")
                            if lineaiz == 1:
                                print ("turn left")
                                print ("forward")
                                if STOP == 1:
                                    print ("STOP")
    return



