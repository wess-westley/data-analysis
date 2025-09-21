# explore_data.py
import pandas as pd
import matplotlib.pyplot as plt

# Load the data - this might take a minute
print("Loading data...")
# df = pd.read_csv('metadata.csv')
df = pd.read_csv(r"C:\Users\user\Desktop\data analysis\metadata.csv\metadata.csv")


# Let's see what's inside!
print("Data shape:", df.shape)  # Shows how many rows and columns
print("\nFirst few rows:")
print(df.head())  # Shows first 5 rows

# Check what columns we have
print("\nColumns in the data:")
print(df.columns.tolist())

# Check for missing data
print("\nMissing values in each column:")
print(df.isnull().sum())