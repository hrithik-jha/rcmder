import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

df=pd.read_csv('songs.csv')
count_matrix = df.loc[:,'song_popularity':'audio_valence']
cosine_sim = cosine_similarity(count_matrix, count_matrix)
indices = pd.Series(df.index, index=df['id'])


def get_recommendations(x, y, cosine_sim=cosine_sim):
    # Get the index of the song that matches the title
    n = x + y
    idx = indices[n]

    # Get the pairwsie similarity scores of all movies with that song
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar songs
    sim_scores = sim_scores[1:11]

    # Get the song indices
    song_indices = [i[0] for i in sim_scores]

    # df['link'].loc[song_indices]=df.loc[song_indices].apply(get_link,axis=1)

    # Return the top 10 most similar songs
    x = df[['song_name', 'artist_name', 'album_names']].iloc[song_indices]
    x = x.to_json(orient='records')
    print(x)
    return df[['song_name', 'artist_name', 'album_names']].iloc[song_indices]

