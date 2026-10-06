def select_features_target(df, target):
    """selects features and target from a dataframe and returns them separately"""
    X = df.drop(columns=[target])
    y = df[target]
    return X, y
