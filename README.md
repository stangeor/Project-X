# Movie Recommender System

## Overview

This project builds a movie recommendation system using collaborative filtering techniques to suggest relevant movies based on user preferences and similarity patterns in rating data.

## Problem Statement

With large movie catalogs, users often struggle to find relevant content. This project addresses that by generating personalized movie recommendations using historical user ratings.

## Approach

* Performed data cleaning and preprocessing using Pandas
* Created a user-item rating matrix
* Applied correlation-based similarity to identify related movies
* Generated recommendations based on user behavior patterns

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook

## Dataset

* Movie titles dataset (`movie_titles.csv`)
* User ratings dataset (`user_ratings.csv`)

## How It Works

1. Load and merge movie titles with user ratings
2. Create a pivot table (user vs movie matrix)
3. Compute similarity scores between movies
4. Recommend movies based on correlation with selected movie

## Sample Output

Example:
If a user likes **Star Wars**, recommended movies include:

* The Empire Strikes Back
* Return of the Jedi
* Raiders of the Lost Ark

## How to Run

1. Clone the repository
2. Open `movie_recommender.ipynb`
3. Run all cells sequentially

## Key Learnings

* Understanding collaborative filtering
* Working with sparse datasets
* Building similarity-based recommendation systems

## Limitations

* Cold start problem (new users/movies)
* No content-based filtering
* Limited evaluation metrics

## Future Improvements

* Implement content-based filtering
* Use matrix factorization (SVD)
* Deploy using Streamlit for UI
* Add evaluation metrics (RMSE, precision@k)

## Author

Stanley George
