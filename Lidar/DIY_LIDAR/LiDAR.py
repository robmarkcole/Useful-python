"""
Forked from https://www.instructables.com/id/Benewake-LiDAR-TFmini-Complete-Guide/
"""
import serial
import time

ser = serial.Serial('/dev/tty.SLAB_USBtoUART', 115200, timeout=1)

ser.write(bytes(b'B'))
ser.write(bytes(b'W'))
ser.write(bytes(2))
ser.write(bytes(0))
ser.write(bytes(0))
ser.write(bytes(0))
ser.write(bytes(1))
ser.write(bytes(6))

while(True):
    while(ser.in_waiting >= 9):
        if((b'Y' == ser.read()) and ( b'Y' == ser.read())):
            
            Dist_L = ser.read()
            Dist_H = ser.read()
            Dist_Total = (ord(Dist_H) * 256) + (ord(Dist_L))
            for i in range (0,5):
                ser.read() 
        print((Dist_Total, 0)) # tuple for plotting with MU



        
