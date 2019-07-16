import time
import pigpio

pi = pigpio.pi()


class Pump:
    def __init__(self, pumpGpio):
        #pi.set_mode(pumpGpio, pigpio.OUTPUT)
        pi.write(pumpGpio, 1)
        self.PUMP_GPIO = pumpGpio

    def run(self, sec):
        pi.write(self.PUMP_GPIO, 0)
        time.sleep(sec)
        pi.write(self.PUMP_GPIO, 1)
