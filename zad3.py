
import pandas as pd
#loading data from a file
df1 = pd.read_csv('train.tsv',sep = '\t',names = ['price', 'num_of_rooms', 'area', 'num_of_floors','address','desc'])
df2 = pd.read_csv('description.csv',header = 0)
#joining data from files
df3 = pd.merge(df1,df2,left_on = 'num_of_floors', right_on = 'liczba', how = 'left').drop('liczba',1)
#saving data to a file
df3.to_csv('out2.csv',index = False)

