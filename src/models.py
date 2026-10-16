from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np 
def train_model(X_train, y_train):
    """
    Fits a linear regression model from X_train and y_train and returns the fitted model

    Args:
        X_train(pandas.DataFrame): the features training sample
        y_train(pandas.Series):  the target training sample

    Returns: 
        model: a fitted linear regression model of X_train and y_train   
    """

    model= LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X, y):
    """
   Takes a model and the dataset sample and  evaluates its perfomance and returns a dictionary of the perfomance metrics

   Args:
        model: a fitted linear regression model
        X(pandas.DataFrame): features DataFrame
        y(pandas.Series): target pandas.Series
    

   Returns: a dictionary with the perfomance metrics(mae, mse, rmse, r2_score)
    
    """

    predictions = model.predict(X)
    mae = mean_absolute_error(y, predictions)
    mse = mean_squared_error(y, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y, predictions)
    

    scores = {
        "mae": mae,
        "mse":mse,
        "rmse":rmse,
        "r2_score":r2
    }

    return scores