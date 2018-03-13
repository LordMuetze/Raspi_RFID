#!/usr/bin/env python
# -*- coding: utf8 -*-
 
import RPi.GPIO as GPIO
import MFRC522
import RFID
 
def sample_func(sample_var):
    # Beispiel Funktion
    # Skript starten, Daten loggen, etc.
    print("Test Funktion wurde aufgerufen")
 
# ...
 
Kartenleser = MFRC522.MFRC522()
authcode = [0, 0, 0, 0, 0, 0, 0, 0, 0] # die ersten 9 Ziffern sind der Authentifizierungscode

while True:
    print(RFID.check(authcode))
