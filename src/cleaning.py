import pandas as pd

def load_data(filename):
    """
    Returns the json data loaded into a Pandas data frame

    Parameters
    ----------
    filename: str
        Name of the json file to be loaded

    Returns
    -------
    df: Pandas df
    """
    df = pd.read_json(filename)
    return df


def make_fraud_column(df):
    """
    Returns a Pandas data frame with a new column ('fraud')
    containing the target label.

    Assumes that the data frame has the columns 'acct_type'

    Parameters
    ----------
    df: Pandas dataframe
        Dataframe used in this case study

    Returns
    -------
    df: Pandas dataframe
        Dataframe with 'fraud' column added

    """
    df['fraud'] = (df['acct_type'] != 'premium').astype(int)
    return df


def deal_with_missings(df):
    """
    Cleans or changes missing values as agreed upon.

    Changes are as follows:
       Drops 'has_header' column

    Parameters
    ----------
    df: Pandas dataframe
        Dataframe used in this case study

    Returns
    -------
    df: Pandas dataframe
        Cleaned dataframe following schema given above
    """
    df.drop('has_header', inplace=True, axis=1)
    return df


def load_and_clean(filename):
    """
    Loads directly from json file and cleans the data for this case study

    Parameters
    ----------
    filename: str
        Name of json file with data in it

    Returns
    -------
    df: Pandas dataframe
        Fully cleanded dataframe
    """
    df = load_data(filename)
    df = make_fraud_column(df)
    return df
