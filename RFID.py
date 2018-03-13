#!/usr/bin/env python
# -*- coding: utf8 -*-
 
import RPi.GPIO as GPIO
import MFRC522

Kartenleser = MFRC522.MFRC522()

def read():
        # Scan for cards    
    (status,TagType) = Kartenleser.MFRC522_Request(Kartenleser.PICC_REQIDL)

    # If a card is found
    if status == Kartenleser.MI_OK:

        # Get the UID of the card
        (status,uid) = Kartenleser.MFRC522_Anticoll()
        print(uid)
        return uid
