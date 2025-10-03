# Import pandas
import pandas as pd

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Filter to movies released in the 1990s
df_90s = netflix_df[(netflix_df["release_year"] >= 1990) & (netflix_df["release_year"] < 2000)]

# Find the most common duration in the 1990s
most_common_duration = df_90s["duration"].mode()[0]
print("Most common duration in 1990s:", most_common_duration)

# Count short action movies (<90 min) in the 1990s
short_movies = df_90s[(df_90s["duration"] < 90) & 
                      (df_90s["type"] == "Movie") & 
                      (df_90s["genre"] == "Action")]
print("Number of short action movies in 1990s:", len(short_movies))
