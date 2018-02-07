from config.configuration import Config
from eva.data import Data
from eva.mllib.ML import Regressor, Classifier, Cluster


def main():
    # get config and set defaults
    config = Config().get_config()
    data = Data(config)

    data = data.loadfrom_excel("./data/UK_DATA.xlsx")
    features = list(["Private_debt", "M4", "GDHI", "GDP", "Labour_prod", "Employment_rate", "Unemployment", "Bank_rate",
                     "5YrBoYldImplInfl", "ERI", "Comm_idx"])

    model = Regressor(config).linear(data[features], data["CPI"])

    print("Model coefficients :")
    print(model.coef_)

    print(model.score(data[features], data["CPI"]))


if __name__ == "__main__":
    main()
