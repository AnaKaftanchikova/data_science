import pandas as pd
import numpy as np

def check_data(in_data):
    return pd.isnull(in_data)

def duplicated_data(in_data):
    return in_data.duplicated()