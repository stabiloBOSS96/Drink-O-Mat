pumps = {
    "pump_1": 16,  # pfeffi
    "pump_2": 20,  # cola
    "pump_3": 21  # jacky
}

setups = {
    "clean_duration": 7,
    "reference_ml_per_sec": 50
}

buttons = {
    "button1": 13,
    "button2": 19,
    "button3": 26
}

drinks = {
    "cola": {
        "displayName": 'Coca Cola',
        "receipt": {
            "pump_2": .8*15
        }
    },
    "jacky_cola": {
        "displayName": 'Jacky Cola',
        "receipt": {
            "pump_3": .8*5,
            "pump_2": .8*15            
        }
    },
    "pfeffi": {
        "displayName": 'Pfeffi',
        "receipt": {
            "pump_1": 1.6
        }
    }
}
glass = {
    "shot_small": {
        "displayName": "Small Shot",
        "quantity": 0.01
    },
    "shot_normal": {
        "displayName": "Normal Shot",
        "quantity": 0.02
    }
}
