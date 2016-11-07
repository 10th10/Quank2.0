# IMPORTS
import time
import RPi.GPIO as GPIO

# VARIABLEN



# SET-UP GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(channel, GPIO.IN)

GPIO.setup(channel, GPIO.OUT)

# WORK

GPIO.input(channel)

GPIO.output(channel, state)

GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)    # dann kein 10 K Widerstand notwendig

os.system('command')

sleep(0.1)

while GPIO.input(channel) == GPIO.LOW:
    time.sleep(0.01)



# ENDE

GPIO.cleanup()