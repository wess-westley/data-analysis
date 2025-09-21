# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Set up the page
st.set_page_config(page_title="COVID-19 Research Explorer", layout="wide")

# Title
st.title("📊 COVID-19 Research Paper Explorer")
st.write("Explore patterns in COVID-19 research papers from the CORD-19 dataset")

# Load data
@st.cache_data  # This makes it load faster after the first time
def load_data():
    return pd.read_csv('cleaned_metadata.csv')

df = load_data()

# Sidebar for filters
st.sidebar.header("🔍 Filters")

# Year filter
years = sorted(df['year'].unique())
selected_years = st.sidebar.slider(
    "Select years:",
    min_value=int(min(years)),
    max_value=int(max(years)),
    value=(2020, 2021)
)

# Filter data based on selection
filtered_df = df[(df['year'] >= selected_years[0]) & (df['year'] <= selected_years[1])]

# Show basic stats
st.header("📈 Basic Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Papers", len(filtered_df))
col2.metric("Years Covered", f"{selected_years[0]} - {selected_years[1]}")
col3.metric("Unique Journals", filtered_df['journal'].nunique())

# Show the charts
st.header("📊 Visualizations")

# Chart 1: Papers by year
st.subheader("Papers Published Each Year")
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(year_counts.index, year_counts.values)
ax.set_xlabel('Year')
ax.set_ylabel('Number of Papers')
st.pyplot(fig)

# Chart 2: Top journals
st.subheader("Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(top_journals.index, top_journals.values)
ax.set_xlabel('Number of Papers')
st.pyplot(fig)

# Chart 3: Word cloud
st.subheader("Common Words in Titles")
all_titles = ' '.join(filtered_df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
fig, ax = plt.subplots(figsize=(12, 6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

# Show sample data
st.header("📋 Sample Data")
if st.checkbox("Show sample of papers"):
    st.dataframe(filtered_df[['title', 'journal', 'year']].head(10))

# Footer
st.markdown("---")
st.markdown("*Data from CORD-19 dataset | Made with Streamlit*")