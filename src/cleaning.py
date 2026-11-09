def fill_absent(df, columns, label="None", only_if_zero=None):
    """
    Returns a new dataFrame with missing blank values in given columns filled
    
    Args:
        df(pandas.DataFrame): dataFrame with our entire data
        columns(list[str]): a list with the  column name with the blank values
        label(str, default value is None): the string used to fill the blank values
        only_if_zero: an optional column used as an anchor to fill blank spaces only when the corresponding value in it is zero

    Returns:
         a dataFrame with our blank values filled with the label           
        
    """
    clean_df = df.copy()
    if only_if_zero is None:
        clean_df[columns]= clean_df[columns].fillna(label)
    else:
        for col in columns:
            mask = (df[col].isnull()) & (df[only_if_zero]==0)
            clean_df.loc[mask, col] = label

    return clean_df

    