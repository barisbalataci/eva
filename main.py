import json
import os
from collections import OrderedDict
#import eva.data_access.load_data as data
from eva.data_access.data import data


def main():
    config=get_config()
    csvFile=data.loadfrom_excel(os.getcwd()+"\\data\\UK_DATA_23Jan17.xlsx")


    #data.load_data()


def get_config():
    config_file = {}
    with open(os.path.join(os.getcwd() + "\\config", "config.json")) as data_file:
        config_file = json.load(data_file, object_pairs_hook=OrderedDict)
    return config_file


if __name__ == "__main__":
    main()
