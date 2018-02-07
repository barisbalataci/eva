import json
import os
from collections import OrderedDict


class Config:

    def __init__(self):
        pass

    def get_config(self):
        config_file = {}
        with open(os.path.join(os.getcwd() + "\\config", "config.json")) as data_file:
            config_file = json.load(data_file, object_pairs_hook=OrderedDict)
        return config_file
