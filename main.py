import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('NetflixOriginals.csv', encoding='ISO-8859-1')
df['Language'] = df['Language'].fillna('')

# Create a boolean mask for English-language movies
is_english_lng = df['Language'].str.contains('English', case=False)
is_multiple_lang = df['Language'].str.contains('/')

# Count movies where English appears in the Language column
english_movie_count = is_english_lng.sum()
total_movie_count = len(df)

# Count movies with multiple languages that do NOT include English
multi_non_english_count = df[is_multiple_lang & ~is_english_lng].shape[0]

# Count single-language, non-English movies
single_non_english_count = total_movie_count - english_movie_count - multi_non_english_count

# Get the top five IMDb rated films 
top_5_imdb_scores = df.nlargest(5, 'IMDB Score')

# Get the bottom five IMDb rated films 
bottom_5_imdb_scores = df.nsmallest(5, 'IMDB Score')

# Calculate the mean IMDb score
imdb_score_mean = df['IMDB Score'].mean()

# Calculate the standard deviation of IMDb scores
imdb_score_std = df['IMDB Score'].std()

# Calculate the mean and standard deviation of movie runtime
runtime_mean = df['Runtime'].mean()
runtime_std = df['Runtime'].std()
runtime_median = df['Runtime'].median()
runtime_iqr = df['Runtime'].quantile(0.75) - df['Runtime'].quantile(0.25)
longest_runtime_row = df.nlargest(1, 'Runtime')[['Title', 'Runtime']].iloc[0]
correlation_coefficient = df['Runtime'].corr(df['IMDB Score'])

print("="*60)
print(f"""Q1: What percentage of all films are primarily in English?
A1: Percentage of English content: {english_movie_count / total_movie_count * 100:.2f}%
""")

print("="*60)
print(f"""Q2: What is the ratio of English-language films to single-language, non-English films?
A2: Ratio of English-language films to single-language, non-English films: {english_movie_count / single_non_english_count:.2f}
""")

print("="*60)
print(f"""Q3: What percentage of films are in multiple languages?
A3: Ratio of multiple language films to all films: {is_multiple_lang.sum() / total_movie_count:.2f}
""")

print("="*60)
print(f"""Q4: Which genres are most common among films with multiple languages?
A4: These are the most common genres in multiple language films:
{df[is_multiple_lang]['Genre'].value_counts()}
The Most common genres in multiple language films is documentary with 17 films.
""")

plt.figure(figsize=(10,6))
plt.hist(df['IMDB Score'], bins=30, color='skyblue', edgecolor='black')
plt.xlabel('IMDB SCORE')
plt.ylabel('Frequency')
plt.title('Distribution of Movie IMDB Scores')
plt.grid(axis='y', alpha=0.75)
# plt.show()

print("="*60)
print(f"""Q5: How are IMDb scores distributed?
      
A5: The mean IMDb score is {imdb_score_mean:.2f} with a standard deviation of {imdb_score_std:.2f}.
The graph shows most scores around the mean, which indicates a normal distribution.
From which we can conclude that the mean gives a good indication of the average film IMDb score.
With a standard deviation of 1.2, we can see that most films are rated between 5.1 and 7.5.
""")

print("="*60)
print(f"""Q6: Which films have the highest and lowest IMDb scores?
A6: Top 5 IMDB scores:
{top_5_imdb_scores.to_string(index=False,  justify='left')}

Bottom 5 IMDB scores:
{bottom_5_imdb_scores.to_string(index=False, justify='left')}
""")

plt.figure(figsize=(10,6))
plt.hist(df['Runtime'], bins=30, color='skyblue', edgecolor='black')
plt.xlabel('Runtime (minutes)')
plt.ylabel('Frequency')
plt.title('Distribution of Movie Runtimes')
plt.grid(axis='y', alpha=0.75)
# plt.show()

print("="*60)
print(f"""Q7: A runtime (in minutes) vs. frequency analysis was performed, resulting in a mean of {runtime_mean:.2f} minutes and a standard deviation of {runtime_std:.2f} minutes.
Does the distribution shown in the graph suggest that these statistics accurately represent the data?
A7: Due to a low amount of high scores in the middle, and a large amount of low scores to the left.
Presents a left skewed distribution, which might distort the mean.
There is a single high value above 200 in the middle, which could be an outlier, which could also distort the mean.
""")

print("="*60)
print(f"""Q8: What alternative statistics would be more robust for skewed runtime data?
A8: The median and the IQR will be more accurate in this case, as they are less affected by outliers and skewed distributions.
""")

print("="*60)
print(f"""Q9: What are the median and IQR of the film runtimes vs frequencies?
A9: The median runtime is {runtime_median} minutes, and the IQR is {runtime_iqr} minutes.

The mean has a typical runtime around 90 minutes, whereas the median is around 100.
With the low IQR that indicates that half the values are close to the median,
it can be which implies that the left skew is more influential on the mean than the high outlier.
""")

print("="*60)
print(f"""Q10: Which film has the longest runtime and what is its duration?
A10: The film with the longest runtime is '{longest_runtime_row['Title']}' with a runtime of {longest_runtime_row['Runtime']} minutes.
""")

plt.figure(figsize=(8,6))
plt.scatter(df['Runtime'], df['IMDB Score'], color='orange', edgecolor='black')
plt.title(f"IMDb Score by Runtime (r = {correlation_coefficient:.2f})")
plt.xlabel("Runtime (minutes)")
plt.ylabel("IMDb Score")
plt.xlim(df['Runtime'].min(), df['Runtime'].max())
plt.ylim(df['IMDB Score'].min(), df['IMDB Score'].max())
plt.grid(True)
plt.show()

print("="*60)
print(f"""Q11: This is the correlation graph between IMDB Score and the runtime. I was told that the correlation coefficient is 0.92. What can be inferred from the coefficient in comparison to the graph?
A11: The plot shows a concentration of points in the middle, which doesn't fit the coefficient of 0.92.
For such a high correlation coefficient, we would expect a more linear graph with less concentration.
""")

print("="*60)
print(f"""Q12: What does the given correlation coefficient indicate about the relationship between runtime and IMDb score?
A12: It indicates a strong positive relationship between runtime and IMDb score, meaning that the longer the runtime the higher the score and vice versa.
""")

print("="*60)
print(f"""Q13: What is the actual correlation coefficient between runtime and IMDb score, and what does it mean?
A13: The true correlation coefficient between runtime and IMDB Score is {correlation_coefficient:.2f}
which indicates a weak negative relationship between runtime and IMDb score, meaning that the longer the runtime the lower the score, in contrast to before.
""")