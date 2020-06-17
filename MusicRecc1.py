'''MUSIC RECOMMENDATION SYSTEM : CONTENT BASED'''

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

df= pd.read_csv('df1.csv', engine='python')
                       
df['index'] = df.index
df.drop('position', inplace=True, axis=1)

features = ['artist', 'genre']

def combine_features(row):
    return row['artist']+ " " +row['genre']

for feature in features:
    df[feature] = df[feature].fillna('') #filling all NaNs with blank string


df["combined_features"] = df.apply(combine_features,axis=1) #applying combined_features() method over each rows of dataframe and storing the combined string in "combined_features" column

df.to_csv("df.csv")

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv = CountVectorizer() #creating new CountVectorizer() object
count_matrix = cv.fit_transform(df["combined_features"]) #feeding combined strings(movie contents) to CountVectorizer() object

cosine_sim = cosine_similarity(count_matrix)

item_similarity_df = pd.DataFrame(cosine_sim)
item_similarity_df.to_csv("item_similarity_df.csv") #save it as a csv file for use in frontend

dfdemo = df[['name', 'position']] #for frontend demo 
dfdemo.to_csv("dfdemo.csv")



    
    

