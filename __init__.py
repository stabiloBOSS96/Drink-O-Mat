import sys
import Barkeeper
from Button import *
import time

#drink = sys.argv[1]
#Barkeeper.mix_drink(drink)
pfeffi_button = Button(config.buttons["button1"])
cola_button = Button(config.buttons["button3"])
jackycola_button = Button(config.buttons["button2"])
while True:
    if pfeffi_button.read_value() == 1:
        print("Please wait...")
        print("Pfeffi processed...")
        Barkeeper.mix_drink("pfeffi")
            
    if cola_button.read_value() == 1:
        print("Please wait...")
        print("Cola processed...")
        Barkeeper.mix_drink("cola")
    
    if jackycola_button.read_value() == 1:
        print("Please wait...")
        print("Jacky cola processed...")
        Barkeeper.mix_drink("jacky_cola")
    #time.sleep(3)


#Barkeeper.clean()
        