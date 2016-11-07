# IMPORTS
import sys, os 
import time
import RPi.GPIO as GPIO
import subprocess

# VARIABLEN DEFINIEREN
## GPIO INPUT-PINS
Q2_PREV = 10
Q2_NEXT = 4
Q2_PLAYPAUSE = 3
Q2_VOLUP = 7
Q2_VOLDOWN = 8
Q2_SHUTDOWN = 0

## GPIO OUTPUT_PINS
Q2_LED_AMP = 0
Q2_LED_PY = 15
Q2_LED_RASP = 0

# SET-UP GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(Q2_PREV, GPIO.IN)
GPIO.setup(Q2_NEXT, GPIO.IN)
GPIO.setup(Q2_PLAYPAUSE, GPIO.IN)
GPIO.setup(Q2_VOLUP, GPIO.IN)
GPIO.setup(Q2_VOLDOWN, GPIO.IN)
GPIO.setup(Q2_SHUTDOWN, GPIO.IN)

GPIO.setup(Q2_LED_AMP, GPIO.OUT)
GPIO.output(Q2_LED_AMP, GPIO.LOW)
GPIO.setup(Q2_LED_PY, GPIO.OUT)
GPIO.output(Q2_LED_PY, GPIO.HIGH)
GPIO.setup(Q2_LED_RASP, GPIO.OUT)
GPIO.output(Q2_LED_RASP, GPIO.LOW)


# ROUTINE

while True:
	try:
		# get actual values from gpio
		
		PREV = GPIO.input(Q2_PREV)
		print PREV
		
		# get right response 
		if PREV == 0:
			subprocess.call(['mpc', 'next'])
			print "PREV gedrueckt"
			
		#elif NEXT ==
		
		#elif 
		
		#elif 
		
		

		
		
		time.sleep(0.5)
		
	except KeyboardInterrupt:
		print "\nExit"
		GPIO.output(Q2_LED_PY, GPIO.LOW)
		GPIO.cleanup()
		sys.exit(0)
		

