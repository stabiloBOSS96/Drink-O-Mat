import config
from Pump import *


def mix_drink(drink):
    for pump, sec in config.drinks[drink]['receipt'].items():
        Pump(config.pumps[pump]).run(sec)


def clean():
    for pump in config.pumps:
        Pump(config.pumps[pump]).run(config.setups['clean_duration'])
