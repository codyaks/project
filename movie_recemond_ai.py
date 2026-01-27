from colorama import init,Fore
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
import time
import sys

init(autoreset=True)

def load_data(filepath='IMDB top 1000.csv'):
    try:
        df = pd.read_csv(filepath)
        df['combined_features']=df['genre'].fillna('')+''+df['overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"Data file not found. Please ensure '{filepath} is in the project directory." + Fore.RESET)
        exit()
movies_df = load_data()

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def list_genres(df):
    return sorted(set(genre.strip() for sublist in df['genre'].dropna().str.split(',') for genre in sublist))
genres=list_genres(movies_df)

def recommend_movies(genre,mood,rating,top_n):
    filtered_df=movies_df
    if genre:
        filtered_df=filtered_df[filtered_df['genre'].str.contains(genre,case=False,na=False)]
    if rating:
        filtered_df=filtered_df[filtered_df['rating']>=rating]
    
    filtered_df=filtered_df.sample(frac=1).reset_index(drop=True)

    recommendation=[]
    for idx,row in filtered_df.iterrows():
         overview = row['overview'] 
         if pd.isna(overview):
                continue
         
