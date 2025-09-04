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

#### **1. Clone the repository**
```bash
git clone https://github.com/your-username/movie-recommendation.git
cd movie-recommendation
```

#### **2. Download Dataset** 
https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system

#### **3. Create a virtual environment**
```bash
python -m venv venv
```

#### **4. Activate the virtual environment**
```bash
.\venv\Scripts\activate
```

#### **5. Install dependencies**
```bash
pip install -r requirements.txt
```

#### **6. Run the Flask application**
```bash
python app.py
```
#### **7. Open this url**
http://127.0.0.1:5000/

## **UI Desgin**
<img width="1000" height="620" alt="image" src="https://github.com/user-attachments/assets/45cf3c67-db7d-4a61-8a6c-6c20dde516ce" />

