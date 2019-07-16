import sys
import Barkeeper
from Button import *
import time
from Lamp import *

pfeffi_button = Button(config.buttons["button1"])
cola_button = Button(config.buttons["button3"])
jackycola_button = Button(config.buttons["button2"])
Lamp().blink()

while True:
    Lamp().on()
    if pfeffi_button.read_value() == 1:
        Lamp().off()
        print("Please wait...")
        print("Pfeffi processed...")
        Barkeeper.mix_drink("pfeffi")
        print("Here you are")
            
    if cola_button.read_value() == 1:
        Lamp().off()
        print("Please wait...")
        print("Cola processed...")
        Barkeeper.mix_drink("cola")
        print("Here you are")
    
    if jackycola_button.read_value() == 1:
        Lamp().off()
        print("Please wait...")
        print("Jacky cola processed...")
        Barkeeper.mix_drink("jacky_cola")
        print("Here you are")


#Barkeeper.clean()
        