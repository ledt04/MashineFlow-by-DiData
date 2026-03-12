import os
import json

DEBUG = True
API_BASE_URL = "http://immvmdidata02.d.immlan.unizh.ch/test"

MACHINE_CONFIG_PATH = "/machine_config.json"

def load_machine_config():
    with open(MACHINE_CONFIG_PATH, 'r') as file:
        config_data = json.data(file)
    return config_data

MACHINE_CONFIG = load_machine_config()