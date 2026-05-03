# 🎬 Item-Based Movie Recommender System

A collaborative filtering recommender system built with Python that suggests movies based on user preferences — inspired by how platforms like Netflix and Spotify generate personalised recommendations.

---

## 📌 Overview

This project implements **item-based collaborative filtering** using the [MovieLens 100K dataset](https://grouplens.org/datasets/movielens/100k/). The core idea is simple: if two movies tend to be rated similarly across many users, they are considered "similar" — and if you liked one, you're likely to enjoy the other.

Rather than relying on movie metadata (genre, director, cast), this approach learns purely from **patterns in user behaviour**, which makes it surprisingly powerful even without domain knowledge about the content itself.

---

## 🗂️ Project Structure

```
item-based-movie-recommender/
│
├── item-based-movie-recommender.ipynb   # Main Jupyter notebook
├── My_Ratings.csv                       # Custom user ratings (my own input)
├── movie_titles__1_.csv                 # Movie ID → Title mapping (1,682 movies)
├── requirements.txt                     # Python dependencies
└── README.md                            # You're reading it
```

> **Note:** The `u.data` file (raw ratings from MovieLens) is not included due to size. Download it directly from [GroupLens](https://grouplens.org/datasets/movielens/100k/).

---

## 🧠 How It Works

The recommendation pipeline follows four main steps:

### 1. Load & Merge Data
Two datasets are loaded and joined:
- `Movie_Id_Titles` — maps numeric item IDs to human-readable movie titles
- `u.data` — tab-separated file with `user_id`, `item_id`, `rating`, and `timestamp`

The timestamp column is dropped as it adds no predictive value here.

### 2. Exploratory Data Analysis
Before modelling, I visualise the rating distributions:
- **Mean rating histogram** — to understand how generous users tend to be
- **Rating count histogram** — to identify popular vs. niche titles
- Most-rated movies and highest-rated movies are examined separately (a movie rated 5/5 by two people isn't comparable to one rated 4.5 by 5,000)

### 3. Single-Movie Correlation (Titanic as a test case)
A user-movie pivot table is built (rows = users, columns = movie titles, values = ratings). I then compute the **Pearson correlation** between Titanic (1997) and every other movie. Movies with fewer than 80 ratings are filtered out to avoid noise from sparse data.

### 4. Full Dataset Recommendation Engine
The same correlation approach is extended across the entire dataset — producing a movie-to-movie correlation matrix. A personal ratings file (`My_Ratings.csv`) feeds into the engine, and the output is a ranked list of recommended titles weighted by my own preferences.

---

## 📊 Dataset

| File | Description |
|------|-------------|
| `u.data` | 100,000 ratings from 943 users on 1,682 movies |
| `Movie_Id_Titles` | Maps `item_id` (int) to movie `title` (string) |
| `My_Ratings.csv` | Custom ratings I assigned to seed the recommender |

**My seed ratings used in this notebook:**

| Movie | My Rating |
|-------|-----------|
| Liar Liar (1997) | 5 |
| Star Wars (1977) | 1 |

The contrasting ratings (5 vs. 1) are intentional — it forces the engine to both seek movies similar to *Liar Liar* and actively down-weight titles similar to *Star Wars*.

---

## ⚙️ Setup & Usage

### Prerequisites
- Python 3.8+
- Jupyter Notebook or JupyterLab

### Installation

```bash
git clone https://github.com/your-username/item-based-movie-recommender.git
cd item-based-movie-recommender
pip install -r requirements.txt
```

### Running the Notebook

```bash
jupyter notebook item-based-movie-recommender.ipynb
```

Then download the MovieLens 100K dataset and place `u.data` and `Movie_Id_Titles` in the same directory before running all cells.

### Customising Recommendations

Edit `My_Ratings.csv` to use your own ratings:

```csv
Movie Name,Ratings
Toy Story (1995),4
Fargo (1996),5
Air Force One (1997),2
```

Movie names must match titles exactly as they appear in `movie_titles__1_.csv`.

---

## 📦 Requirements

```
pandas
numpy
matplotlib
seaborn
```

See `requirements.txt` for pinned versions.

---

## 🔍 Key Concepts

**Item-Based Collaborative Filtering**
Computes similarity between items (movies) rather than between users. This approach scales better than user-based filtering when the user base is large, and tends to produce more stable recommendations since item relationships change less frequently than user preferences.

**Pearson Correlation Coefficient**
Used to measure the linear relationship between the rating vectors of two movies. A correlation of 1.0 means two movies are rated identically across all users; 0 means no relationship.

**Minimum Period Threshold (`min_periods=80`)**
Only movies with at least 80 co-rated users are considered when computing correlations. This prevents movies with very few reviews from appearing as "perfect matches" due to coincidental overlap.

---

## 📈 Sample Output

Running the engine with the seed ratings above produces a ranked list like:

```
Silence of the Lambs, The (1991)    4.89
Shawshank Redemption, The (1994)    4.75
Fargo (1996)                        4.71
...
```

(Actual output will vary depending on the full dataset and your seed ratings.)

---

## 🚧 Limitations & Next Steps

- **Sparsity:** The user-movie matrix is highly sparse — most users have only rated a small fraction of available movies, which limits correlation quality.
- **Cold Start:** New movies or new users with no rating history cannot be recommended or used as seeds.
- **Scale:** For production use, approximate nearest neighbour methods (e.g., Faiss, Annoy) would replace the brute-force correlation matrix.

Potential improvements:
- [ ] Matrix factorisation (SVD / NMF) for better handling of sparse data
- [ ] Weighted hybrid approach combining content-based and collaborative signals
- [ ] Simple Streamlit or Gradio front-end for interactive recommendations

---

## 📚 References

- [MovieLens 100K Dataset — GroupLens Research](https://grouplens.org/datasets/movielens/100k/)
- F. Maxwell Harper and Joseph A. Konstan (2015). *The MovieLens Datasets: History and Context.* ACM Transactions on Interactive Intelligent Systems.
- [Collaborative Filtering — Wikipedia](https://en.wikipedia.org/wiki/Collaborative_filtering)

---

## 📝 Licence

The MovieLens dataset is provided by GroupLens under their own [terms of use](https://grouplens.org/datasets/movielens/100k/).
