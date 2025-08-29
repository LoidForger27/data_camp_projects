"""
Investigating Netflix Movies (1990s) — script version

Source dataset: netflix_data.csv
Expected columns:
- show_id, type, title, director, cast, country, date_added,
  release_year, duration, description, genre

What this script does:
1) Loads the CSV into a DataFrame.
2) Keeps only rows where type == "Movie".
3) Filters to movies released in the 1990s (1990 <= year < 2000).
4) Plots a histogram of durations (minutes).
5) Filters to Action movies and counts how many are < 90 minutes,
   first with a for-loop, then with a vectorized .sum().
""" 
import pandas as pd
import matplotlib.pyplot as plt


def main(csv_path: str = "netflix_data.csv") -> None:
    # Read in the Netflix CSV as a DataFrame
    netflix_df = pd.read_csv(csv_path)

    # Subset for type "Movie"
    netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

    # Filter: movies released in or after 1990
    subset = netflix_subset[netflix_subset["release_year"] >= 1990]

    # Filter: movies released before 2000 (i.e., 1990s)
    movies_1990s = subset[subset["release_year"] < 2000]

    # Visualize duration distribution
    plt.hist(movies_1990s["duration"])
    plt.title("Distribution of Movie Durations in the 1990s")
    plt.xlabel("Duration (minutes)")
    plt.ylabel("Number of Movies")
    plt.show()

    # Optional: save an approximate peak duration if you eyeball the chart
    duration = 100  # placeholder from the original exercise
    print(f"Approximate duration peak (eyeballed): {duration} minutes")

    # Keep only Action movies
    action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

    # Count short action movies (< 90 minutes): loop approach
    short_movie_count = 0
    for _, row in action_movies_1990s.iterrows():
        if row["duration"] < 90:
            short_movie_count += 1
        else:
            short_movie_count = short_movie_count

    print(f"Short Action movies (< 90 min) — loop count: {short_movie_count}")

    # Faster, vectorized count
    short_count_fast = (action_movies_1990s["duration"] < 90).sum()
    print(f"Short Action movies (< 90 min) — vectorized count: {short_count_fast}")


if __name__ == "__main__":
    main()
