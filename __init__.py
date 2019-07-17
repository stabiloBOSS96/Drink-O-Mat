import sys
import Barkeeper
from Button import *
import time
from Lamp import *

pfeffi_button = Button(config.buttons["button1"])
cola_button = Button(config.buttons["button3"])
jackycola_button = Button(config.buttons["button2"])
Lamp().blink()

print("""/
 ____       _       _          ___        __  __       _   
|  _ \ _ __(_)_ __ | | __     / _ \      |  \/  | __ _| |_ 
| | | | '__| | '_ \| |/ /____| | | |_____| |\/| |/ _` | __|
| |_| | |  | | | | |   <_____| |_| |_____| |  | | (_| | |_ 
|____/|_|  |_|_| |_|_|\_\     \___/      |_|  |_|\__,_|\__|
                                                           
                                _           _   _           
 _ __  _ __ ___  ___  ___ _ __ | |_ ___  __| | | |__  _   _ 
| '_ \| '__/ _ \/ __|/ _ \ '_ \| __/ _ \/ _` | | '_ \| | | |
| |_) | | |  __/\__ \  __/ | | | ||  __/ (_| | | |_) | |_| |
| .__/|_|  \___||___/\___|_| |_|\__\___|\__,_| |_.__/ \__, |
|_|                                                   |___/ 
   _  _ __        ______ _           _   _ _                                                             
 _| || |\ \      / / ___(_)_ __ ___ | | | | |__  _ __ ___ _ __  _ __ ___  _   _ ___  ___ _   _ _ __ ___  
|_  ..  _\ \ /\ / / |  _| | '_ ` _ \| | | | '_ \| '__/ _ \ '_ \| '_ ` _ \| | | / __|/ _ \ | | | '_ ` _ \ 
|_      _|\ V  V /| |_| | | | | | | | |_| | | | | | |  __/ | | | | | | | | |_| \__ \  __/ |_| | | | | | |
  |_||_|   \_/\_/  \____|_|_| |_| |_|\___/|_| |_|_|  \___|_| |_|_| |_| |_|\__,_|___/\___|\__,_|_| |_| |_|
                                                                                                         

""")

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
        