def fill_absent(df, columns, label="None"):
    """
    Returns a new dataFrame with missing blank values in given columns filled
    
    Args:
        df(pandas.DataFrame): dataFrame with our entire data
        columns(list[str]): a list with the  column name with the blank values
        label(str, default value is None): the string used to fill the blank values

    Returns:
         a dataFrame with our blank values filled with the label           
        
    """
    clean_df = df.copy()
    clean_df[columns]= clean_df[columns].fillna(label)
    return clean_df

    