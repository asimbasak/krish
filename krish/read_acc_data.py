#===============================================================
###   Get Time(s) and Acc(g) data
#===============================================================
import pandas as pd

def read_csv_file(file_name):
    return pd.read_csv(file_name)

def get_time_acc(filename,TimeCol, AccCol):
    df = pd.read_csv(filename)

    time = df[TimeCol]
    acc = df[AccCol]

    return time, acc

#===============================================================