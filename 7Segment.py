# -*- coding: utf-8 -*-
from time import *
import RPi.GPIO as GPIO

liste_0 = [1,2,4,6,7,8]
liste_1 = [4,6]
liste_2 = [1,2,5,6,8]
liste_3 = [2,4,5,6,8]
liste_4 = [4,5,6,7]
liste_5 = [2,4,5,7,8]
liste_6 = [1,2,4,5,7,8]
liste_7 = [4,6,8]
liste_8 = [1,2,4,5,6,7,8]
liste_9 = [2,4,5,6,7,8]



segments = [40,38,36,37,35,33,31,29]
GPIO.setmode(GPIO.BOARD)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)

digits = [16,12,10,8]
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit,GPIO.HIGH)


def an(nummer):
    global segments
    global liste_0
    global liste_1
    global liste_2
    global liste_3
    global liste_4
    global liste_5
    global liste_6
    global liste_7
    global liste_8
    global liste_9
    global test

    exec("for index in liste_"+str(nummer)+": real_index = index-1; GPIO.output(segments[real_index],GPIO.HIGH)")
            

def aus():
    global segments
    for segment in segments:
        GPIO.output(segment,GPIO.LOW)

zeit1 = time()
zeit2 = time()

while True:
        
    for digit in digits:
        GPIO.output(digit,GPIO.LOW)
        if digit == 16:
            an(1)
            aus()
        else:
            an(0)
            aus()     
        GPIO.output(digit,GPIO.HIGH) 


GPIO.cleanup()