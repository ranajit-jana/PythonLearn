import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
import numpy as np
import ast
import seaborn as sea
df = pd.read_csv("titles.csv")

#What are the most common genres?
#gendf = df['genres']
#all_genres = gendf.apply(ast.literal_eval).explode()
#counts = all_genres.value_counts()
#most_common_genre = counts.idxmax()
#most_common_count = counts.max()
#print(f"Most common genre: {most_common_genre} ({most_common_count} times)")
#############################################################################
#which genres have the highest average IMDb scores?
dfnad = df.dropna(subset=["imdb_score", "genres"])
dfnad['genres'] = dfnad['genres'].apply(ast.literal_eval)

print(type(dfnad))

df_exploded = dfnad.explode('genres')
print(type(f_exploded))

genre_imdb_scores = df_exploded.groupby('genres')['imdb_score'].mean().sort_values(ascending=False)
print(genre_imdb_scores)
#higest_score_genre = genre_imdb_scores.idxmax()
#higest_score_max = genre_imdb_scores.max()
#print(f" Genre {higest_score_genre} scored highest average value {higest_score_max}")

###################################################################
#How do movies compare to TV shows in terms of IMDb rating and number of votes?
#df_filtered = df.dropna(subset=['imdb_score', 'imdb_votes'])
#comparison = df_filtered.groupby('type')[['imdb_score', 'imdb_votes']].mean().round(1)
#print(comparison)
######################################################################
#Is there a relationship between IMDb votes and score 
#df = df.dropna(subset=['imdb_score', 'imdb_votes'])
#correlation = df['imdb_score'].corr(df['imdb_votes'])
#print(correlation)
##########################
#plt.scatter(df['imdb_votes'], df['imdb_score'], alpha=0.5)
#plt.xlabel('IMDB Votes')
#plt.ylabel('IMDB Score')
#plt.title('Relationship between IMDB Votes and IMDB Score')
#plt.show()

##################################################################
#Does genre popularity change over years in this dataset?
#df = df.dropna(subset=['tmdb_popularity', 'release_year', 'genres'])
#df['genres'] = df['genres'].apply(ast.literal_eval)
#df = df.explode('genres')
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
