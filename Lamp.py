import pigpio
import time

pi = pigpio.pi()

class Lamp:
    pi.set_mode(2, pigpio.INPUT)
    
    def off(self):
        pi.write(2,1)
    
    def on(self):
        pi.write(2,0)
    
    def blink(self):
        for i in range (5):
            self.on()
            time.sleep(1)
            self.off()
            time.sleep(1)