# -*- coding: utf-8 -*-
from time import *
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

segments =  [40,38,36,37,35,33,31,29]
# 7seg_segment_pins (11,7,4,2,1,10,5,3) +  100R inline

print("\n") 
for segment in segments:
    print(segment)
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)


digits = [8,10,12,16]
# 7seg_digit_pins (12,9,8,6) digits 0-3 respectively
print("\n") 
for digit in digits:
    print(digit)
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)



def an(nummer):
    GPIO.output(nummer,1)
def aus(nummer):
    GPIO.output(nummer,0)





while True:
    an(7)
    an(4)
    sleep(2)
    aus(7)
    aus(4)
    sleep(2)
    

    


