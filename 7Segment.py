# -*- coding: utf-8 -*-
from time import sleep
import RPi.GPIO as GPIO

null = [1,2,4,6,7,8]
eins = [4,6]
zwei = [1,2,5,6,8]
drei = [2,4,5,6,8]
vier = [4,5,6,7]
fuenf = [2,4,5,7,8]
sechs = [1,2,4,5,7,8]
sieben = [4,6,8]
acht = [1,2,4,5,6,7,8]
neun = [2,4,5,6,7,8]
punkt = [3]



segments = [40,38,36,37,35,33,31,29]
GPIO.setmode(GPIO.BOARD)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)

digits = [16,12,10,8]
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)


def an(nummer):
    global segments
    global null
    global eins
    global zwei
    global drei
    global vier
    global fuenf
    global sechs
    global sieben
    global acht
    global neun
    global test
    if nummer == 1:
        for index in eins:
            real_index = index-1
            print("Index:\t"+str(index))
            print("Real-Index\t"+str(real_index))
            GPIO.output(segments[real_index],GPIO.HIGH)

def aus():
    global segments
    for segment in segments:
        GPIO.output(segment,GPIO.LOW)

while True:
    for digit in digits:
        GPIO.output(digit,GPIO.LOW)
        an(1)
        sleep(5)
        aus()
        
        GPIO.output(digit,GPIO.HIGH)

        GPIO.cleanup()
