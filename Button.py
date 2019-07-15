import config
import pigpio

pi = pigpio.pi()


class Button:
    def __init__(self, gpio):
        pi.set_mode(gpio, pigpio.INPUT)
        pi.set_pull_up_down(gpio, pigpio.PUD_DOWN)
        self.BUTTON_GPIO = gpio

    def read_value(self):
        if pi.read(config.buttons["button1"]) == 1:
            return 1
        else:
            return 0