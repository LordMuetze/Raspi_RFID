#!/usr/bin/env python
# -*- coding: utf8 -*-
 
import RPi.GPIO as GPIO
import MFRC522
from time import sleep

Kartenleser = MFRC522.MFRC522()

def read():
        # Scan for cards    
    (status, TagType) = Kartenleser.MFRC522_Request(Kartenleser.PICC_REQIDL)
    # If a card is found
    if status == Kartenleser.MI_OK:

        # Get the UID of the card
        (status,uid_raw) = Kartenleser.MFRC522_Anticoll()
        uid = int(str(uid_raw[0])+str(uid_raw[1])+str(uid_raw[2])+str(uid_raw[3])+str(uid_raw[4]))
        print("\n------------------------------------------------------------------------------\n")
        print(uid)
        print("\n------------------------------------------------------------------------------\n")
        return uid

def check(UID=[]):
        # Scan for cards    
    (status, TagType) = Kartenleser.MFRC522_Request(Kartenleser.PICC_REQIDL)
    # If a card is found
    if status == Kartenleser.MI_OK:

        # Get the UID of the card
        (status,uid_raw) = Kartenleser.MFRC522_Anticoll()
        uid = int(str(uid_raw[0])+str(uid_raw[1])+str(uid_raw[2])+str(uid_raw[3])+str(uid_raw[4]))
        print("\n------------------------------------------------------------------------------\n")
        print(uid)
        print("Permitted: " + str(uid in UID))
        print("\n------------------------------------------------------------------------------\n")
        return uid in UID

def erkennen():
        # Scan for cards    
    (status, TagType) = Kartenleser.MFRC522_Request(Kartenleser.PICC_REQIDL)
    # If a card is found
    if status == Kartenleser.MI_OK:
        print("\n------------------------------------------------------------------------------\n")
        print("Karte erkannt")
        print("\n------------------------------------------------------------------------------\n")
        erkannt = True
        return erkannt
