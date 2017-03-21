import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

motion = 13
SecLEDPin = 12

GPIO.setup(motion , GPIO.IN)
GPIO.setup(SecLEDPin, GPIO.OUT)

while (True):
	sleep(0.4)
	current_state = GPIO.input(motion)
	if current_state == 1: 
		GPIO.output(SecLEDPin, True)
		sleep(0.4)
		print 10
	GPIO.output(SecLEDPin, False)
	sleep(1)	
