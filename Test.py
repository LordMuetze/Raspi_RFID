import RFID

while True:
    zugang = RFID.check()
    if zugang:
        print("Herein spaziert!")
    if not zugang:
        print("Zugang verweigert")
    sleep(0.5)

