# clean_data.py
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
print("Loading data...")
#df = pd.read_csv(r"C:\Users\user\Desktop\data analysis\metadata.csv\metadata.csv" )

df = pd.read_csv(
    r"C:\Users\user\Desktop\data analysis\metadata.csv\metadata.csv",
    dtype=str
)

# Let's clean it up!
print("Cleaning data...")

# 1. Keep only important columns
important_columns = ['title', 'abstract', 'publish_time', 'journal', 'authors', 'source_x']
df_clean = df[important_columns].copy()

# 2. Handle missing values
df_clean['abstract'] = df_clean['abstract'].fillna('No abstract available')
df_clean['journal'] = df_clean['journal'].fillna('Unknown journal')

# 3. Extract year from publish_time
df_clean['year'] = pd.to_datetime(df_clean['publish_time'], errors='coerce').dt.year
df_clean['year'] = df_clean['year'].fillna(2020)  # Fill missing years with 2020

# 4. Remove rows without titles
df_clean = df_clean.dropna(subset=['title'])

print("Cleaned data shape:", df_clean.shape)
print("\nSample of cleaned data:")
print(df_clean.head())

# Save cleaned data
df_clean.to_csv('cleaned_metadata.csv', index=False)
print("\nSaved cleaned data to 'cleaned_metadata.csv'")