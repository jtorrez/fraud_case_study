import pandas as pd

def load_data(filename):
    df = pd.read_json(filename)
    return df

def make_fraud_column(df):
    df['fraud'] = (df['acct_type'] != 'premium').astype(int)
    return df

def load_and_clean(filename):
    df = load_data(filename)
    df = make_fraud_column(df)
    return df
