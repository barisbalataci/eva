import pandas as pd


class data:
    def __init__(self, config):
        self.config = config

    def loadfrom_csv(datafile):
        try:
            return pd.read_csv(datafile)
        except Exception as e:
            print("Error : "+ str(e))

    def loadfrom_excel(datafile):
        try:
            return pd.read_excel(datafile)
        except Exception as e:
            print("Error : " + str(e))

    def loadfrom_df(df):
        print(df)

    def transform(datafile):
        print(file)
