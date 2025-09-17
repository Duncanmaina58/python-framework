import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Title
st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year
    return df

df = load_data()

# Sidebar filter
years = st.sidebar.slider("Select Year Range", 2015, 2023, (2019, 2021))
filtered = df[(df["year"] >= years[0]) & (df["year"] <= years[1])]

# Display data sample
st.subheader("Data Sample")
st.write(filtered.head())

# Publications over time
st.subheader("Publications Over Time")
year_counts = filtered["year"].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title("Publications by Year")
st.pyplot(fig)

# Top journals
st.subheader("Top Journals")
top_journals = filtered["journal"].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax)
st.pyplot(fig)

# Word cloud
st.subheader("Word Cloud of Titles")
titles = " ".join(str(t) for t in filtered["title"].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
