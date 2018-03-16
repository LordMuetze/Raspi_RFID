import RFID
from time import sleep
import LED

LED.aus()

while True:
    if RFID.erkennen():
        LED.an()
        sleep(1)
    else:
        LED.aus()
        sleep(0.2)
    
