import pandas as pd
import numpy as np

def open_csv_pandas(file_path):
    "To open a .csv. Insert the path and it will return the df"
    df = pd.read_csv(file_path, sep=',', encoding='UTF-8', index_col=0)
    return df


def get_type_cuisine(cuisine):
    "Function to group the restaurants following the type of cuisine, as there are many different types"
    if 'Modern' in cuisine or "Fusion" in cuisine:
        return 'Modern'
    elif 'Contemporary' in cuisine:
        return 'Contemporary'
    elif 'Creative' in cuisine:
        return 'Creative'
    elif 'Regional' in cuisine:
        return 'Regional'
    elif 'Classic' in cuisine or "Traditional" in cuisine:
        return 'Classic'
    else:
        return 'Other' 