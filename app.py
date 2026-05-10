import streamlit as st
import pickle
import numpy as np
import requests

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = np.load('similarity.npy')

API_KEY = st.secrets["TMDB_API_KEY"]

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        data = requests.get(url, timeout=5).json()
        path = data.get('poster_path')
        return "https://image.tmdb.org/t/p/w500" + path if path else None
    except:
        return None

def recommend(movie):
    idx = movies[movies['title'] == movie].index[0]
    distances = similarity[idx]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    titles, posters = [], []
    for i in movie_list:
        titles.append(movies.iloc[i[0]]['title'])
        posters.append(fetch_poster(movies.iloc[i[0]]['movie_id']))
    return titles, posters

st.set_page_config(page_title="CineMatch", page_icon="🎬", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

* { font-family: 'Inter', sans-serif; }
.stApp { background: #141414; color: #fff; }
#MainMenu, header, footer { visibility: hidden; }

.hero {
    text-align: center;
    padding: 64px 0 48px 0;
}
.hero h1 {
    font-size: 48px;
    font-weight: 600;
    color: #fff;
    margin: 0 0 12px 0;
    letter-spacing: -1.5px;
}
.hero p {
    font-size: 14px;
    font-weight: 300;
    color: #666;
    margin: 0;
}

.stSelectbox label {
    font-size: 11px !important;
    font-weight: 500 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: #555 !important;
}
.stSelectbox > div > div {
    background: #1f1f1f !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 8px !important;
    color: #fff !important;
    font-size: 14px !important;
}

.stButton > button {
    background: #fff;
    color: #141414;
    font-weight: 600;
    font-size: 13px;
    border: none;
    border-radius: 8px;
    padding: 14px;
    width: 100%;
}
.stButton > button:hover {
    background: #e0e0e0;
    color: #141414;
}

.section-title {
    font-size: 13px;
    font-weight: 500;
    color: #555;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin: 48px 0 20px 0;
}

.movie-title {
    font-size: 12px;
    font-weight: 500;
    color: #ccc;
    margin-top: 10px;
    line-height: 1.4;
}

.no-poster {
    background: #1f1f1f;
    border: 1px solid #2a2a2a;
    border-radius: 8px;
    aspect-ratio: 2/3;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #333;
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

img { border-radius: 8px !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>CineMatch</h1>
    <p>Pick a movie. Discover five more you'll love.</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    selected_movie = st.selectbox("Film", movies['title'].values)
    clicked = st.button("Get Recommendations")

if clicked:
    with st.spinner(""):
        titles, posters = recommend(selected_movie)

    st.markdown(f'<p class="section-title">Because you liked {selected_movie}</p>', unsafe_allow_html=True)

    cols = st.columns(5)
    for col, title, poster in zip(cols, titles, posters):
        with col:
            if poster:
                st.image(poster, use_container_width=True)
            else:
                st.markdown('<div class="no-poster">No poster</div>', unsafe_allow_html=True)
            st.markdown(f'<p class="movie-title">{title}</p>', unsafe_allow_html=True)