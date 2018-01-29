
import config.config_UK_CPI  as config
from eva.data_access import load_data

def main():
    load_data.load_data(config)

if __name__ == "__main__": 
    main()
    