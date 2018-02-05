
import json
import os
from collections import OrderedDict

def get_config():
    config_file = {}
    with open(os.path.join(os.getcwd() + "\\config", "config.json")) as data_file:
        config_file = json.load(data_file, object_pairs_hook=OrderedDict)
    return config_file
