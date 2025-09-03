from flask import Flask, render_template, request
from model.recommender import get_recommendations, movies

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommended_movies = []
    if request.method == 'POST':
        movie_name = request.form['movie_name']
        recommended_movies = get_recommendations(movie_name)
    
    # Pass all movie titles for dropdown autocomplete
    all_movies = movies['title'].tolist()
    return render_template('index.html', movies=all_movies, recommended=recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
