import serial

port = "/dev/ttyS0"    # Raspberry Pi 3

serial = serial.Serial(port, baudrate = 9600, timeout=1)
print "Starting Receive"
text = ""
while (text != "exit"): 
    text = serial.readline()
    #text = text[:-1] 
    text = text.replace("\r\n", "")		    
    if (text != ""):
       print ("Droid: " + text)
