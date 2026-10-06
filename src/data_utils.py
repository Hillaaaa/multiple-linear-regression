import pandas as pd

def load_data(filepath):
    """loads data from a given file path and returns a pandas DataFrame"""
    if filepath.lower().endswith(".csv"):
        df = pd.read_csv(filepath)
    elif filepath.lower().endswith(".xlsx"):
        df = pd.read_excel(filepath)
    elif filepath.lower().endswith(".json"):
        df = pd.read_json(filepath)
    else:
        raise ValueError("Unsupported file type: " + filepath)
    return df 

def inspect_data(df):
    """ inspects a dataframe and returns various information about it"""
    print("__head__")
    print(df.head())
    print("__shape__")
    print(df.shape)
    print("__info__")
    df.info()
    print("__describe__")
    print(df.describe())
    print("__null values__")
    print(df.isnull().sum())

         
