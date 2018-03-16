# -*- coding: utf-8 -*-
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

def an():
    GPIO.output(11,GPIO.HIGH)

def aus():
    GPIO.output(11,GPIO.LOW)
