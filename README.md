\# 🎬 CineMatch — Movie Recommendation System

**Live demo:**[Click here
](https://ayush-cinematch.streamlit.app/)

A content-based movie recommendation system that suggests similar films based on what you pick. Built with Python and deployed using Streamlit.



\## How it works



CineMatch analyzes movie metadata — genres, keywords, cast, crew, and overview — and converts them into vectors using CountVectorizer. It then computes cosine similarity between all movies to find the closest matches to your selection.



\## Tech Stack



\- \*\*Python\*\* — core language

\- \*\*Pandas \& NumPy\*\* — data processing

\- \*\*Scikit-learn\*\* — CountVectorizer and cosine similarity

\- \*\*NLTK\*\* — text stemming

\- \*\*Streamlit\*\* — web interface

\- \*\*TMDB API\*\* — movie poster fetching



\## Dataset



\[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) from Kaggle.



\## Run locally



1\. Clone the repository

```bash

&#x20;  git clone https://github.com/ayush2002mondal/cinematch.git

&#x20;  cd cinematch

```



2\. Install dependencies

```bash

&#x20;  pip install -r requirements.txt

```



3\. Add your TMDB API key — create `.streamlit/secrets.toml`:

```toml

&#x20;  TMDB\_API\_KEY = "your\_api\_key\_here"

```



4\. Run the app

```bash

&#x20;  streamlit run app.py

```



\## Project Structure



```

cinematch/

├── app.py                  # Streamlit web app

├── movie recommender.ipynb # Model building notebook

├── movies.pkl              # Processed movie data

├── similarity.npy          # Precomputed similarity matrix

└── requirements.txt        # Dependencies

```

