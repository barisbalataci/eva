from config.configuration import get_config
from eva.data import data
from eva.mllib.ML import ML_algoritms


def main():
    # get config and set defaults
    config = get_config()
    dt = data(config)

    df = dt.loadfrom_excel("./data/UK_DATA.xlsx")
    print(df.head(5))

    features = list(["Private_debt", "M4", "GDHI", "GDP", "Labour_prod", "Employment_rate", "Unemployment", "Bank_rate",
                     "5YrBoYldImplInfl", "ERI", "Comm_idx"])

    algoritm = ML_algoritms(config)
    model = algoritm.linear_regression(df["CPI"],df[features])

    print("Model coefficients :",model.coef_)


if __name__ == "__main__":
    main()
