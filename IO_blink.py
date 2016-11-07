# IMPORTS
import os 
import time
import RPi.GPIO as GPIO

# VARIABLEN

i = 0


# SET-UP GPIO
 
GPIO.setmode(GPIO.BCM)

#GPIO.setup(channel, GPIO.IN)

GPIO.setup(15, GPIO.OUT)
GPIO.setup (10, GPIO.IN)

GPIO.output(15, GPIO.LOW)
GPIO.input (10)


# WORK

while i < 10: 

	if i % 2:
		GPIO.output(15, GPIO.HIGH)
	else:
		GPIO.output(15, GPIO.LOW)

	
	if GPIO.input(10):
		print('Input was HIGH')
	else:
		print('Input was LOW')
	i = i + 1 
	time.sleep(2)

# ENDE

GPIO.cleanup()