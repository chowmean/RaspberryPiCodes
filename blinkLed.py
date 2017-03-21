import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

blinkCount = 7
count=0
LEDPin = 22
SecLEDPin = 12

GPIO.setup(LEDPin , GPIO.OUT)
GPIO.setup(SecLEDPin, GPIO.OUT)

while (count < blinkCount):
	GPIO.output(LEDPin, True)
	GPIO.output(SecLEDPin, False)
	sleep(1)
	print count
	GPIO.output(SecLEDPin, True)
	GPIO.output(LEDPin, False)
	sleep(1)
	count=count+1	
GPIO.output(SecLEDPin, False)
