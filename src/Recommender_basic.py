import pandas

columns = ['user_id', 'item_id', 'rating', 'time_stamp']
user_ratings_path = "C:\\python projects\\gfg_recommender.tsv"
movie_path = "C:\\python projects\\Movie_Id_Titles.csv"

ratings_dataset = pandas.read_csv(user_ratings_path, sep = '\t', names = columns)
movie_dataset = pandas.read_csv(movie_path)

data_frame = pandas.merge(ratings_dataset, movie_dataset, on = 'item_id')

ratings = pandas.DataFrame(data_frame.groupby('title')['rating'].mean())
ratings['no_of_ratings'] = pandas.DataFrame(data_frame.groupby('title')['rating'].count())

movie_matrix = data_frame.pivot_table(index = 'user_id', columns = 'title', values = 'rating')

starWars_ratings = movie_matrix['Star Wars (1977)']

similar_to_starWars = movie_matrix.corrwith(starWars_ratings)

corr_starWars = pandas.DataFrame(similar_to_starWars, columns = ['Correlation'])
corr_starWars.dropna(inplace = True)

corr_starWars.sort_values('Correlation', ascending  = False).head(10)
corr_starWars = corr_starWars.join(ratings['no_of_ratings'])

corr_starWars = corr_starWars[corr_starWars['no_of_ratings'] > 100].sort_values('Correlation', ascending = False).head(20)

print(corr_starWars.head(5))