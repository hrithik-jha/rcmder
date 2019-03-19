import pandas as pd
from rake_nltk import Rake
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
#import pickle

#Database Initialization
df = pd.read_csv('IMDB-Movie-Data.csv')
df = df[['Title','Genre','Description','Director','Actors',]]

#Data Cleaning
df['Key_words'] = ""

attributes = []

df['Attributes'] = ""

for index, row in df.iterrows():
    genre = row['Genre']
    genre = genre.lower()
    genre = genre.split(',')
    attributes.extend(genre)
    director = row['Director']
    director = director.replace(" ","")
    director = director.replace("-","")
    director = director.replace(".","")
    director = director.lower()
    director = director.split(',')
    attributes.extend(director)
    actor = row['Actors']
    actor = actor.replace(" ","")
    actor = actor.replace("-","")
    actor = actor.replace(".","")
    actor = actor.lower()
    actor = actor.split(',')
    attributes.extend(actor)
    plot = row['Description']
    r = Rake()
    r.extract_keywords_from_text(plot)
    key_words_dict_scores = r.get_word_degrees()
    attributes.extend(key_words_dict_scores.keys())

    finalatt = list(attributes)
    attr = ' '.join(finalatt)
    row['Attributes'] = attr
    attributes.clear()

#Vectorization
count = CountVectorizer()
count_matrix = count.fit_transform(df['Attributes'])
cosine_sim = cosine_similarity(count_matrix, count_matrix)
indi = pd.Series(df.Title)
indices = indi

#Recommendation
def recommendations(idx, cosine_sim = cosine_sim):
    recommended_movies = []
    reccs = []
    #idx = indices[indices == title].index[0]
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
    top_10 = list(score_series.iloc[1:11].index)
    for i in top_10:
        recommended_movies.append(list(df.index)[i])
    for i in recommended_movies:
        reccs.append(indices[i])
    return reccs


#x = input('Enter the movie: ')
#rm = recommendations(x)

#print("The recommended movies are: ")
#for i in rm:
#    print(indices[i])