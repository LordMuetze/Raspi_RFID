import RFID
from time import sleep

while True:
    zugang = RFID.check()
    if zugang:
        print("Herein spaziert!")
    if zugang == False:
        print("Zugang verweigert")
    sleep(0.5)

