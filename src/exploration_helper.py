import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


###### FUNCTIONS TO SPEED UP THE DRAFT EXPLORATION PROCESS


def get_inf_count(df:pd.DataFrame) -> dict:
    '''
    Find the number of inf/-inf values per column in dataframe
    Using dictionary comprehension
    Parameters:
        df: pandas data frame
    Returns:
        python dictionary with the key as a column name and number of inf as the value
    '''
    return {
        col: df[df[col].isin([np.inf, -np.inf])].shape[0] for col in df.columns
    }

def get_inf_columns(df:pd.DataFrame) -> list:
    '''
    Find the number of inf/-inf values per column in dataframe
    Using dictionary comprehension
    Parameters:
        df: pandas data frame
    Returns:
        python list with name of columns that contain the infinity numbers
    '''
    return [col for col in df.columns if df[df[col].isin([np.inf, -np.inf])].shape[0] > 0]

def replace_inf_with_nan(df:pd.DataFrame, cols:list([str]), impute:bool=False) -> pd.DataFrame:
    '''
    Replase np.inf with np.nan
    Parameters:
        df: pandas data frame
        cols: list of columns with infinite values, default -> all columns of dataframe
        impute: boolean, if True - impute with zeros
    Return:
        df: pandas data frame with inf values replaced with np.nan or 0
    '''

    for col in cols:
        df[col] = df[col].replace(dict.fromkeys([np.inf, -np.inf], np.nan))

    if impute:
        for col in cols:
            df[col] = df[col].fillna(0)

    return df

def duplicated_rows(df:pd.DataFrame) -> pd.DataFrame:
    '''
    Print the number of rows with duplicates (first appearance)
    Print total number of rows with duplicates (all appearances)
    Parameters:
        df: pandas data frame
    Returns:
        pandas data frame with duplicated rows
    '''
    print(f'Rows with duplicates: {df[df.duplicated()].shape[0]}')
    print(f'All rows that presented more than once: {df[df.duplicated(keep=Fasle)].shape[0]}')

    return df[df.duplicated()]

def get_numeric_columns(df:pd.DataFrame) -> list[str]:
    '''
    Create a list with names of numeric columns
    Parameters:
        df: pandas data frame
    Returns:
        numerical: list of numerical column names
    '''
    numerical = []
    for col in df:
        if df[col].dtype.kind in 'buifc':
            numerical.append(col)
    return numerical
