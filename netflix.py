import pandas as pd

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_titles.csv")

# Filter for movies released in 1990
data_1990 = netflix_df[netflix_df['release_year'] == 1990]

# Select the 'duration' column
data_duration = data_1990[['duration']]

# Count occurrences of each duration
counts = data_duration['duration'].value_counts()

# Find the maximum count
max_count = counts.max()

# Find the durations with the maximum count
durations = counts[counts == max_count]
print(durations)
