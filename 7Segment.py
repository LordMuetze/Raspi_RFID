# -*- coding: utf-8 -*-
from time import sleep
import RPi.GPIO as GPIO

null = [11,7,4,2,1,10]
eins = [4,7]
zwei = [11,7,5,1,2]
drei = [11,7,5,4,2]
vier = [10,5,7,4]
fuenf = [11,10,5,4,2]
sechs = [11,10,1,2,4,5]
sieben = [11,7,4]
acht = [11,7,4,2,1,5,10]
neun = [10,11,7,5,4,2]
test = [1,2,3,4,5,7,10,11]



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
