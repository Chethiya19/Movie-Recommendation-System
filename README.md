# 🎬 Movie Recommendation System

A **Python Flask web application** that recommends movies based on content similarity (genres). Users can select a movie from the list and get instant recommendations.  

---

## **Features**

- Content-based movie recommendations using **genres**.
- **Autocomplete movie search** for easier selection.
- **Responsive and modern UI** with cards and gradient background.
- Lightweight and memory-efficient using **NearestNeighbors** instead of huge cosine similarity matrices.
- Works with large datasets (like MovieLens 62k movies).  

---

## **Installation**

```bash
Clone the repository
git clone https://github.com/your-username/movie-recommendation.git
cd movie-recommendation

### Create a virtual environmen
python -m venv venv

### Activate the virtual environment
.\venv\Scripts\activate

### Install dependencies
pip install -r requirements.txt

### Run the Flask application
python app.py

http://127.0.0.1:5000/
