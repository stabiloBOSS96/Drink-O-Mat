import sys
import Barkeeper
from Button import *

#drink = sys.argv[1]
#Barkeeper.mix_drink(drink)
pfeffi_button = Button(config.buttons["button1"])
while True:
    if pfeffi_button.read_value() == 1:
        print("Please wait...")
        print("Pfeffi processed...")
        Barkeeper.mix_drink("pfeffi")


Barkeeper.clean()
        