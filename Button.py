import config
import pigpio

pi = pigpio.pi()


class Button:
    def __init__(self, gpio):
        pi.set_mode(self, gpio, pigpio.INPUT)
        pi.set_pull_up_down(self, gpio, pigpio.PUD_DOWN)

    def read_value(self):
        if pigpio.read(config.buttons["button1"]) == 1:
            return 1
        else:
            return 0