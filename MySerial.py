import serial
ser = serial.Serial('COM26')  # open serial port Windows
#ser = serial.Serial('/dev/ttyUSB0')  # open serial port Linux / Mac
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()             # close port