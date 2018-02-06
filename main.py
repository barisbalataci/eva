from config.configuration import get_config
from eva.data import Data
from eva.mllib.ML import Regressor


def main():
    # get config and set defaults
    config = get_config()
    data = Data(config)

    data = data.loadfrom_excel("./data/UK_DATA.xlsx")
    features = list(["Private_debt", "M4", "GDHI", "GDP", "Labour_prod", "Employment_rate", "Unemployment", "Bank_rate",
                     "5YrBoYldImplInfl", "ERI", "Comm_idx"])

    regressor = Regressor(config)
    model = regressor.linear(data[features], data["CPI"])

    print("Model coefficients :")
    print(model.coef_)




if __name__ == "__main__":
    main()
