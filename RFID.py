#!/usr/bin/env python
# -*- coding: utf8 -*-
 
import RPi.GPIO as GPIO
import MFRC522

Kartenleser = MFRC522.MFRC522()

def check(authcode):
        # Scan for cards    
    (status,TagType) = Kartenleser.MFRC522_Request(Kartenleser.PICC_REQIDL)

    # If a card is found
    if status == Kartenleser.MI_OK:

        # Get the UID of the card
        (status,uid) = Kartenleser.MFRC522_Anticoll()
        print(uid)
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        # Select the scanned tag
        Kartenleser.MFRC522_SelectTag(uid)
        # Authenticate
        status = Kartenleser.MFRC522_Auth(Kartenleser.PICC_AUTHENT1A, 8, key, uid)
        print("\n"+str(status))
        # Check if authenticated
        if status == Kartenleser.MI_OK:
            # Read block 8
            data = Kartenleser.MFRC522_Read(8)
            print (data)
            if data[:9] == authcode:
                return True
            else:
                return False