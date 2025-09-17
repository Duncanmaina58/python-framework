
---


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load data
df = pd.read_csv("metadata.csv")

# Convert publish_time to datetime
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year

# Basic stats
print(df.info())
print(df.describe())

# Missing values
print("Missing values:\n", df.isnull().sum())

# Papers per year
year_counts = df["year"].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

# Top journals
top_journals = df["journal"].value_counts().head(10)
sns.barplot(x=top_journals.values, y=top_journals.index)
plt.title("Top Journals Publishing COVID-19 Research")
plt.show()

# Word cloud for titles
titles = " ".join(str(t) for t in df["title"].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
