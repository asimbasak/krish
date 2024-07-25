import pandas as pd

def read_csv_file(file_name):
    df = pd.read_csv(file_name)
    return df

def get_time_acc_from_df(df, TimeCol, AccCol):
    time = df[TimeCol]
    acc = df[AccCol].fillna(0) * 9.80665 * 1000
    return time, acc

def get_time_acc_from_csv(file_name, TimeCol, AccCol):
    df = pd.read_csv(file_name)
    time = df[TimeCol]
    acc = df[AccCol].fillna(0) * 9.80665 * 1000
    return time, acc
