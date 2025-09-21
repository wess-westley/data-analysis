# make_charts.py
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

# Load cleaned data
print("Loading cleaned data...")
df = pd.read_csv('cleaned_metadata.csv')

# Chart 1: Papers by year
plt.figure(figsize=(10, 6))
year_counts = df['year'].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.title('Number of COVID-19 Papers Published Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('papers_by_year.png')
print("Saved chart: papers_by_year.png")

# Chart 2: Top journals
plt.figure(figsize=(12, 8))
top_journals = df['journal'].value_counts().head(10)
plt.barh(top_journals.index, top_journals.values)
plt.title('Top 10 Journals Publishing COVID-19 Research')
plt.xlabel('Number of Papers')
plt.tight_layout()
plt.savefig('top_journals.png')
print("Saved chart: top_journals.png")

# Chart 3: Word cloud of titles
plt.figure(figsize=(12, 8))
all_titles = ' '.join(df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Most Common Words in Paper Titles')
plt.tight_layout()
plt.savefig('wordcloud.png')
print("Saved chart: wordcloud.png")

# Chart 4: Papers by source
plt.figure(figsize=(10, 6))
source_counts = df['source_x'].value_counts().head(8)
plt.pie(source_counts.values, labels=source_counts.index, autopct='%1.1f%%')
plt.title('Where the Papers Come From (Sources)')
plt.tight_layout()
plt.savefig('sources_pie.png')
print("Saved chart: sources_pie.png")

print("\nAll charts saved! Check your folder for the image files.")