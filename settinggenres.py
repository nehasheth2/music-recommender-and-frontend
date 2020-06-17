# -*- coding: utf-8 -*-
"""
Setting Genres for App
optional : can alter needed genres """

import pandas as pd

songs = pd.read_csv("songs.csv")
songs.drop_duplicates(subset=['spotify_id', 'name', 'artist'], keep='first', inplace=True)


genres = ['pop', 'rap', 'edm', 'hip hop', 'rock', 'classic rock', 'pop rap', 
          'post-teen pop', 'modern rock', 'pop rock', 'indie pop', 'country', 
          'dance pop', 'punk', 'electric blues', 'jazz blues',
          'lofi chill', 'dubstep', 'chillstep', 
          'trap', 'soft rock', 'indie pop', 'filmi', 'indian pop',
          'r&b', 'house', 'alternative rock', 'viral pop', 'metal',
          'blues-rock', 'lo-fi beats', 'desi pop', 'hollywood', 'classical', 'jazz', 'meditation',
          'funk', 'indian classical', 'canadian pop', 'funk metal', 'pop rap', 'desi', 
          'uk pop', 'europop', 'country rock', 'indie poptimism', 'art pop', 'psychedelic rock',
          'chicago rap', 'toronto rap', 'singer-songwriter','indie r&b', 'modern country rock', 
          'quiet storm', 'new romantic', 'progressive electro house', 'indie folk', 'disco', 'punk',
          'emo', 'uk hip hop', 'uk dance', 'social media pop', 'modern bollywood', 'west coast rap',
          'acoustic pop', 'lounge', 'classic soul', 'deep house', 'reggae', 'reggae fusion', 
          'downtempo', 'salsa', 'trance', 'modern blues rock', 'hip house', 'electro', 'drum and bass',
          'early music', 'desi hip hop', 'british blues', 'modern hard rock', 'chill guitar',
          'ambient pop', 'world fusion', 'retro soul', 'techno', 'banjo', 'instrumental acoustic guitar', 'classical guitar',
          'blues-rock guitar', 'pop urbaine', 'pop punk', 'country pop', 'punjabi pop', 'pop house', 'teen pop', 'indie electropop',
          'alternative pop rock', 'popwave', 'album rock', 'roots rock', 'indie rock', 'lovers rock', 'stoner rock', 'indian rock',
          'desi hip hop', 'hindi hip hop', 'tropical house', 'big room', 'progressive electro house', 'canadian pop', 'urban contemporary',
          'folk rock', 'chamber pop', 'deep indie r&b', 'g funk', 'progressive metal', 'alternative metal']


df = songs[songs['genre'].isin(genres)]

df.size
df.shape
df.to_csv("df1.csv") #save it and then delete INDEX column from csv file'''