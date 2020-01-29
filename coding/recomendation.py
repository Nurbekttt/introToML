import pandas as pd
import numpy as np

ratings_df = pd.read_csv("ratings.csv")
movies_df = pd.read_csv("movies.csv")

data = pd.merge(movies_df, ratings_df, on='movieId')

ratings = pd.DataFrame(data.groupby('title')['rating'].mean())  
ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count()) 
moviemat = data.pivot_table(index ='userId',columns ='title', values ='rating')

starwars_user_ratings = moviemat['Toy Story (1995)'] 
liarliar_user_ratings = moviemat['GoldenEye (1995)'] 
similar_to_starwars = moviemat.corrwith(starwars_user_ratings) 
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)

corr_starwars = pd.DataFrame(similar_to_starwars, columns =['Correlation']) 
corr_starwars.dropna(inplace = True)
#corr_starwars.sort_values('Correlation', ascending = False).head(10) 
corr_starwars = corr_starwars.join(ratings['num of ratings']) 
print(corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation', ascending = False).head())
corr_liarliar = pd.DataFrame(similar_to_liarliar, columns =['Correlation']) 
corr_liarliar.dropna(inplace = True)   
corr_liarliar = corr_liarliar.join(ratings['num of ratings']) 
print(corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation', ascending = False).head()) 
