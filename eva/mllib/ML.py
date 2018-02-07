from eva.mllib.sklearn.ML import Regressor_Sklearn


class Regressor:

    def __init__(self, config):
        if config["platform"] == "sklearn":
            self.lib = Regressor_Sklearn()

    def linear(self, input, output):
        return self.lib.linear(input, output)


class Classifier:
    pass


class Cluster:
    pass
