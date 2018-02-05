from eva.mllib.sklearn.ML_algoritms import  ML_algoritms_sklearn

# from eva.mllib.spark import ML_algoritms

class ML_algoritms:

    def __init__(self, config):
        if (config["platform"] == "sklearn"):
            self.lib = ML_algoritms_sklearn


    def linear_regression(self, y, features):
        return self.lib.linear_regression(y,features)

