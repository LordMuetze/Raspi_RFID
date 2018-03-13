#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
from time import *

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
Kartenleser = MFRC522.MFRC522()

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = Kartenleser.MFRC522_Request(Kartenleser.PICC_REQIDL)

    # If a card is found
    if status == Kartenleser.MI_OK:
        print "Card detected"
    
    # Get the UID of the card
    (status,uid) = Kartenleser.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == Kartenleser.MI_OK:

        # Print UID
        print "UID: "+str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])
    
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        Kartenleser.MFRC522_SelectTag(uid)

        # Authenticate
        status = Kartenleser.MFRC522_Auth(Kartenleser.PICC_AUTHENT1A, 32, key, uid)

        # Check if authenticated
        if status == Kartenleser.MI_OK:
            Kartenleser.MFRC522_Read(8)
            Kartenleser.MFRC522_StopCrypto1()
        
        sleep(2)

