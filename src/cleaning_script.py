import pandas as pd
import json

def convert_json_to_df(raw_json):
    df = pd.read_json(raw_json)
    return df

def clean_df(df):
    df['null_count'] = df.isnull().sum(axis=1)
    ##create new dataframe with only numeric values for FSM
    numeric_df = df.drop(['country', 'currency', 'description', 'email_domain', \
        'listed', 'name', 'org_desc', 'org_name', 'payee_name', 'payout_type', \
        'previous_payouts',  'ticket_types', 'venue_address', 'venue_country', \
        'venue_name', 'venue_state', 'has_header', 'sale_duration', 'venue_latitude', 'venue_longitude', 'org_facebook', 'org_twitter' ], axis=1)
    clean_df = numeric_df.dropna(axis=0, subset=['delivery_method', 'event_published'])
    return clean_df

def clean_df_to_json(df):
    return df.to_json()

def clean(json_str):
    df = convert_json_to_df(json_str)
    return clean_df_to_json(clean_df(df))
