import pandas as pd

def read_csv_file(file_name):
    """
    Reads a CSV file and returns a DataFrame.

    Parameters:
    file_name (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The data from the CSV file.
    """
    return pd.read_csv(file_name)
