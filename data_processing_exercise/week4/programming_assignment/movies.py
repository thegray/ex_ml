# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 22:18:33 2018

@author: Bangun
## reference for this case study, see: 
## http://www.gregreda.com/2013/10/26/using-pandas-on-the-movielens-dataset/
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = r'ml-100k'

#### rating

rating_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratingpath = path + '\\u.data'
rating = pd.read_table(ratingpath, sep='\t', names=rating_cols, encoding='latin-1')

#### movies

movies_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
moviepath = path + '\\u.item'
movies = pd.read_table(moviepath, sep='|', names=movies_cols, usecols=range(5), encoding='latin-1')

#### user

user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_csv(r'ml-100k\u.user', sep='|', names=user_cols, encoding='latin-1')

#### merge movies and rating

movie_ratings = pd.merge(movies, rating)
movie_ratings_users = pd.merge(movie_ratings, users)

#### exercise

most_rated = movie_ratings_users.groupby('title').size().sort_values(ascending=False)[:25]

most_rated2 = movie_ratings_users.title.value_counts()[:25]

movie_stats = movie_ratings_users.groupby('title').agg({'rating':[np.size, np.mean]})
movie_stats.head()

# sort by rating average
movie_stats.sort_values([('rating', 'mean')], ascending=False).head()

# see movies that have been rated > 100 times
atleast_100 = movie_stats['rating']['size'] >= 100
movie_stats[atleast_100].sort_values([('rating','mean')], ascending=False)[:15]

most_50 = movie_ratings_users.groupby('movie_id').size().sort_values(ascending=False)[:50]

# see age of users distribution 
users.age.plot.hist(bins=30)
plt.title("Distribution of users' ages")
plt.ylabel('count of users')
plt.xlabel('age')

# categories users to group
labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79']
movie_ratings_users['age_group'] = pd.cut(movie_ratings_users.age, range(0, 81, 10), right=False, labels=labels)
movie_ratings_users[['age', 'age_group']].drop_duplicates()[:10]

movie_ratings_users.groupby('age_group').agg({'rating': [np.size, np.mean]})

movie_ratings_users.set_index('movie_id', inplace=True)
by_age = movie_ratings_users.loc[most_50.index].groupby(['title','age_group'])
by_age.rating.mean().head(15)

by_age.rating.mean().unstack(1).fillna(0)[10:20]

movie_ratings_users.reset_index('movie_id', inplace=True)

pivoted = movie_ratings_users.pivot_table(index=['movie_id', 'title'], columns=['gender'], values='rating', fill_value=0)
pivoted.head()

pivoted['diff'] = pivoted.M - pivoted.F
pivoted.head()

pivoted.reset_index('movie_id', inplace=True)
disagreements = pivoted[pivoted.movie_id.isin(most_50.index)]['diff']
disagreements.sort_values().plot(kind='barh', figsize=[9, 15])
plt.title('Male vs. Female Avg. Ratings\n(Difference > 0 = Favored by Men)')
plt.ylabel('Title')
plt.xlabel('Average Rating Difference');
