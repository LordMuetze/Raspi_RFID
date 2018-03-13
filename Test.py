#!/usr/bin/env python
# -*- coding: utf8 -*-
 
import RPi.GPIO as GPIO
import MFRC522
 
def sample_func(sample_var):
    # Beispiel Funktion
    # Skript starten, Daten loggen, etc.
    print("Test Funktion wurde aufgerufen")
 
# ...
 
Kartenleser = MFRC522.MFRC522()
authcode = [0, 0, 0, 0, 0, 0, 0, 0, 0] # die ersten 9 Ziffern sind der Authentifizierungscode

while True:
    

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
                sample_func("\n"+str(data))
            #elif ...
