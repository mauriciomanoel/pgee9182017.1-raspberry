import RPi.GPIO as GPIO
import time
led_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
try:
	while 1:
		print("led ligado")
		GPIO.output(led_pin, True)
		time.sleep(1)
		print("led desligado")
		GPIO.output(led_pin, False)
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
print("fim")	
		

