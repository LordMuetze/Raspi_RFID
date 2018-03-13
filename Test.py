import RFID
from time import sleep

while True:
    zugang = RFID.check([128234125162181])
    if zugang == True:
        print("Herein spaziert!")
    if zugang == False:
        print("Zugang verweigert")
    sleep(0.2)
