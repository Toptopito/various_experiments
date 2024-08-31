# Test codes for data analysis of the hospital price transparency dataset


# import required libraries
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline #valid only for Jupyter notebooks
import seaborn as sns
pd.Series.__unicode__ = pd.Series.to_string

# read dataset
hospital_prices_file_path = "C:/Users/vladc/OneDrive/Documents/Project Legacy/hospital_prices.csv"

hospital_prices = pd.read_csv(hospital_prices_file_path, nrows=100000)
print(hospital_prices.describe())

