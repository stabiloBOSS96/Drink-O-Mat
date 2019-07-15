import sys
import Barkeeper
from Button import *

#drink = sys.argv[1]
#Barkeeper.mix_drink(drink)
cola_button = Button(config.buttons["button1"])
while True:
    cola_button.read_value()