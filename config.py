import os
from configparser import ConfigParser

# CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config/config.ini')
config = None
con = None

def get_settings(CONFIG_PATH):
    global config
    if config is None:
        config = ConfigParser()
        config.read(CONFIG_PATH)
    return config