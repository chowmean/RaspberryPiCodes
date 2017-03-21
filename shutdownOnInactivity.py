import RPi.GPIO as GPIO
from time import sleep
from subprocess import call
GPIO.setmode(GPIO.BCM)

motion = 13
SecLEDPin = 12

GPIO.setup(motion , GPIO.IN)
#GPIO.setup(SecLEDPin, GPIO.OUT)
count = 0
while (True):
	sleep(0.4)
	current_state = GPIO.input(motion)
	if current_state == 1: 
		#GPIO.output(SecLEDPin, True)
		print "hello sir , DOnt move"
		sleep(0.4)
		print 10
#	GPIO.output(SecLEDPin, False)
	sleep(1)
	count = count + 1
	if(count == 10):
		print "congrats 10 sec completed"
		#call(["shutdown", "-h","now"])
		
