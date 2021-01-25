import numpy as np
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

m = np.array([[11, 12, 13], [11, 12, 13], [11, 12, 13]])

print(m[0, 0])

ledpin = m[0, 0]
GPIO.setup(ledpin, GPIO.OUT)

i = 0
while i < 2:
    print("led turning on")
    GPIO.output(ledpin, GPIO.HIGH)
    time.sleep(0.5)
    print("led turning off")
    GPIO.output(ledpin, GPIO.LOW)
    time.sleep(0.5)