from sklearn import linear_model


class Regressor_Sklearn:

    def __init__(self):
        pass

    def linear(self, input, output):
        model = linear_model.LinearRegression()
        model.fit(input, output)
        return model
