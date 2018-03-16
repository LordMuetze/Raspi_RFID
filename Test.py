<<<<<<< HEAD
import osos.chdir('/home/pi/Python/Raspi_RFID')
import lcd
lcd.lcd_init()
=======
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
    
>>>>>>> ad9294dc32f76850182b26583bdb96419b96c9a6
