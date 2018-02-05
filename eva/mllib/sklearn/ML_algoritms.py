from sklearn import linear_model


class ML_algoritms_sklearn():

    def linear_regression( y, features):
        model = linear_model.LinearRegression()
        model.fit(features, y)
        return model
