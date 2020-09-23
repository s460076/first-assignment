
import pandas as pd
#loading data from a file
df_realty = pd.read_csv('train.tsv',sep='\t',names=['price', 'num_of_rooms', 'area', 'num_of_floors', 'address', 'desc'])
df_desc = pd.read_csv('description.csv', header=0)
#joining data from files
df_realty = pd.merge(df_realty, df_desc, left_on='num_of_floors', right_on='liczba', how='left').drop('liczba', 1)
#saving data to a file
df_realty.to_csv('out2.csv', index=False)

