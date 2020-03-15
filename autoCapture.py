import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep

triggerPin = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(triggerPin, GPIO.OUT)
capturedTime = -1


def capture():
	GPIO.output(triggerPin, GPIO.HIGH)
	# hold button on for 50 ms
	sleep(.05)
	GPIO.output(triggerPin, GPIO.LOW)

try:
	while True:
		now = datetime.now()
		if now.minute % 10 == 0 and now.minute != capturedTime:
			capture()
			capturedTime = now.minute
			print("Photo Captured: " + now.strftime("%H:%M:%S"))
finally:
	GPIO.cleanup()
