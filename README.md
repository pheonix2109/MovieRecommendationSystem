# MovieRecommendationSystem

GOAL:

    The goal is to make suggestions for the users. The intuition behind this sort of recommendation system is that if a user liked a particular movie, he/she might like a movie similar to it.

    - Default page
    
    ![alt text](https://github.com/pheonix2109/MovieRecommendationSystem/blob/main/Screenshot%202025-04-01%20170509.png?raw=true)

    
    - Output Page
    ![alt text](https://github.com/pheonix2109/MovieRecommendationSystem/blob/main/Screenshot%202025-04-01%20170758.png?raw=true)
    
ABOUT DATASET:

    https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
    
    There are 2 csv files "tmdb_5000_credits.csv" with columns as follows:
    - movie_id, 
    - title, 
    - cast, 
    - crew 
    and "tmdb_5000_movies.csv" with columns as follows:
    - budget,
    - genres,
    - homepage,
    - id,
    - keywords,
    - original_language,
    - original_title,
    - overview,
    - popularity,
    - production_companies,
    - release_date,
    - revenue,
    - runtime,
    - spoken_languages,
    - status,
    - tagline,
    - title,
    - vote_average,
    - vote_count
    

APPROACH FOR THE PROJECT

    1. Content-Based Filtering
        How It Works: 
        - Recommends movies based on the features of items (movies) that a user has previously liked.
        - Features Used: Genre, actors, directors, keywords, etc.
        - If a user likes Action Movies, the system suggests other movies with the Action tag.
   
NOTEBOOK:

    https://github.com/pheonix2109/MovieRecommendationSystem/blob/main/MovieRecommenderSystem.ipynb

