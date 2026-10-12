import pandas as pd

def load_data(filepath, **kwargs):
    """Loads a data file into a pandas DataFrame
    
    Args:
         filepath: string for holding the path for the data file. Accepts extensions such as .csv, .data, .xlsx and .json
         **kwargs: extra instructions that are passed in the underlying pandas reader for example sep and na_values
    
    Returns:
         a pandas.DataFrame

    Raises:
           ValueError: if we pass an unsupported file type 
           """
    if filepath.lower().endswith((".csv",".data")):
        df = pd.read_csv(filepath,**kwargs)
    elif filepath.lower().endswith(".xlsx"):
        df = pd.read_excel(filepath, **kwargs)
    elif filepath.lower().endswith(".json"):
        df = pd.read_json(filepath,**kwargs)
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

         
