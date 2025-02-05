###############################################
# Scipt to move servo motors. The IMU for 
# the EKF animation is mounted on the servo.
# This allows remote motion of the IMU.
# AUthor: Arasch Lagies
# Created on : 6/29/2020
# Last Update: 
#
# Call: python moveServo.com
###############################################
import RPi.GPIO as GPIO
import time

PORT = 19

GPIO.setmode(GPIO.BOARD)

GPIO.setup(PORT, GPIO.OUT)

p = GPIO.PWM(PORT, 20)

p.start(7.5)

try:
    while True:
        p.ChangeDutyCycle(7.5)  # turn towards 90 degree
        time.sleep(1) # sleep 1 second
        p.ChangeDutyCycle(2.5)  # turn towards 0 degree
        time.sleep(1) # sleep 1 second
        p.ChangeDutyCycle(12.5) # turn towards 180 degree
        time.sleep(1) # sleep 1 second 
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()