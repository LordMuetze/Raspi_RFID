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


def an(nummer,anzeige=1):
    global segments
    global digits
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

    GPIO.output(digits[anzeige-1],GPIO.LOW)
    exec("for index in liste_"+str(nummer)+": real_index = index-1; GPIO.output(segments[real_index],GPIO.HIGH)")
    #GPIO.output(digits[anzeige-1],GPIO.HIGH)        

def aus():
    global segments
    for segment in segments:
        GPIO.output(segment,GPIO.LOW)
    for digit in digits:
        GPIO.output(digit,GPIO.HIGH)

def zahl(zahl):
    zeit1 = time()
    zahl_str = str(abs(zahl))

    if zahl < 0 or zahl > 9999:
        print("Sorry, diese Zahl kann nicht angezeigt werden")

    i = 1
    for ch in zahl_str:
        an(ch,i)
        aus()
        i += 1
    zeit2 = time()
    print(zeit2-zeit1)
