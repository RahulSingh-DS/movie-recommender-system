# movie-recommender-system
🎬 Content-based Movie Recommender System using NumPy &amp; Streamlit | Cosine Similarity | Real-time recommendations



# 🎬 Movie Recommender System

A content-based movie recommendation system built using **NumPy, Pandas, and Streamlit**.
This project suggests movies similar to a selected movie using **cosine similarity**.

---

## 🚀 Features

* 🎥 Recommend top 5 similar movies
* ⚡ Fast similarity computation using vectorization
* 🧠 Content-based filtering (no user data required)
* 🌐 Interactive UI with Streamlit

---

## 🛠️ Tech Stack

* Python
* NumPy
* Pandas
* Scikit-learn
* Streamlit

---

## 📊 How It Works

1. Movie features like **genres, keywords, cast, and crew** are combined
2. Converted into text data (tags)
3. Transformed into vectors using **Bag of Words**
4. Cosine similarity is calculated between movies
5. Top 5 most similar movies are recommended

---

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Live Demo

* *

---

## 📂 Project Structure

```
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── setup.sh
├── Procfile
└── Movie Recommender System.ipynb
```

---

## 🔥 Future Improvements

* Add movie posters
* Add search autocomplete
* Improve UI (Netflix-style)
* Deploy on cloud

---

## 👨‍💻 Author

Rahul Singh
