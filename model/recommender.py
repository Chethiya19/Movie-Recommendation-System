import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors

# Load movies and ratings
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# Content-based filtering using genres
count_vectorizer = CountVectorizer(token_pattern='[a-zA-Z0-9]+')
count_matrix = count_vectorizer.fit_transform(movies['genres'])

# Use NearestNeighbors to find similar movies (memory-efficient)
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(count_matrix)

def get_recommendations(movie_title, num=5):
    """
    Returns a list of recommended movie titles similar to the given movie.
    """
    if movie_title not in movies['title'].values:
        return ["Movie not found in database"]
    
    idx = movies[movies['title'] == movie_title].index[0]
    distances, indices = model.kneighbors(count_matrix[idx], n_neighbors=num+1)
    recommended_indices = indices.flatten()[1:]  # skip the first one (itself)
    return movies['title'].iloc[recommended_indices].tolist()


# Optional: standalone test
if __name__ == "__main__":
    movie = "Toy Story (1995)"
    recommendations = get_recommendations(movie)
    print(f"Recommendations for '{movie}':")
    for m in recommendations:
        print(m)
