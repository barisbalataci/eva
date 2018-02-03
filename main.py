import config.config_UK_CPI as config
import eva.data_access.load_data as data


def main():
    data.load_data(config)


if __name__ == "__main__":
    main()
