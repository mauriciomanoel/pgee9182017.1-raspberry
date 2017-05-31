import serial
import time

port = "/dev/ttyS0"    # Raspberry Pi 3

serial = serial.Serial(port, baudrate = 9600, timeout=3)
print "starting"
text = ""
while (text != "exit\n"): 
    send = raw_input()
    if (send != ""):
       serial.write("PC: " + send + " \r\n")	
