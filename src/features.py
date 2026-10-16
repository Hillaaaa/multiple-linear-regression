import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
def select_features_target(df, target,features=None):
    """selects features and target from a dataframe and returns them separately

    Args:
        df(pandas.DataFrame): a DataFrame where our models and features are gotten from
        target(str): a string for the column name of the target for our model
        features(list[str], optional): column names to be used as our model's features. If omitted every column except the target is used

    Returns:
        X: 2d pandas.DataFrame for the features
        y: a 1d pandas.series of the target         
    
        """
    if features:
        X = df[features]
    else:
        X = df.drop(columns=[target])
    y = df[target]
    return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    """
    Splits our features and targets into separate training and test samples

    Args:
        X(pandas.DataFrame): a pandas.DataFrame of our features
        y(pandas.series): a pandas.series of our target
        test_size(interger, default is 0.2): the ratio for test sample to training sample
        random_state(integer, default is 42): this for us to always produce reproducible results for comparison purposes

    Returns:
        X_train: a pandas.DataFrame for the features training sample
        X_test: a pandas.DataFrame for the features test sample
        y_train: a pandas.series for the target training sample        
        y_test: a pandas.series for the target test sample
    """
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test