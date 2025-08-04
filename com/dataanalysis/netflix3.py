import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import numpy as np
import ast
import seaborn as sea
df = pd.read_csv("titles.csv")


#Does genre popularity change over years in this dataset?
df = df.dropna(subset=['tmdb_popularity', 'release_year', 'genres'])
df['genres'] = df['genres'].apply(ast.literal_eval)
df = df.explode('genres')
pivot_table = df.pivot(index='release_year', columns='genres', values='tmdb_popularity')
plt.figure(figsize=(12, 8))
sea.heatmap(pivot_table, cmap='viridis')
plt.title('Average Popularity by Genre and Year')
plt.show()
#genre_year_popularity = df.groupby(['genres', 'release_year'])['tmdb_popularity'].mean().reset_index()
#top_genres = genre_year_popularity['genres'].value_counts().head(3).index
#for genre in top_genres:
#    subset = genre_year_popularity[genre_year_popularity['genres'] == genre]
#    plt.plot(subset['release_year'], subset['tmdb_popularity'], label=genre)
#plt.title("TMDB Popularity over Years by Genre")
#plt.xlabel("Release Year")
#plt.ylabel("Avg TMDB Popularity")
#plt.legend()
#plt.grid(True)
#plt.tight_layout()
#plt.show()

###############################################################################

#How does age certification differ across genres or content types?

#df = df.dropna(subset=['age_certification', 'genres', 'type'])

#df['genres'] = df['genres'].apply(ast.literal_eval)
#df = df.explode('genres')
#df.to_csv("certification.csv")

#counts = df.groupby(['genres', 'type', 'age_certification']).size().unstack(fill_value=0)
#print(counts)
#grouped = df.groupby(['genres', 'type', 'age_certification']).size().reset_index(name='count')

# Plot using seaborn
#plt.figure(figsize=(14, 6))
#sea.barplot(data=grouped, x='genres', y='count', hue='age_certification', ci=None)

#lt.title('Age Certification Count by Genre (Aggregated across MOVIE and SHOW)')
#plt.xticks(rotation=45)
#plt.ylabel('Number of Titles')
#plt.xlabel('Genre')
#plt.legend(title='Age Certification')
#plt.tight_layout()
#plt.show()
