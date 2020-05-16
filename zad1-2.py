
import pandas as pd 
df = pd.read_csv('train.tsv',sep = '\t',names = ['price', 'num_of_rooms', 'area', 'num_of_floors','address','desc']) 
#calculation of the average
avg_price = round(df['price'].mean(),3) 
import csv 
#saving the average to a file
with open('out0.csv', 'w') as file:
    writer = csv.writer(file) 
    writer.writerow([avg_price]) 
 

#adding a new column
df['square_meter_price'] = round(df['price']/df['area'],3)
#writing specific lines to a file
with open('out1.csv', 'w') as file_2:
    writer = csv.writer(file_2) 
    for index, row in df.iterrows():
        if row['num_of_rooms'] >=3 and row['square_meter_price'] < df['square_meter_price'].mean():
            writer.writerow([row['num_of_rooms'], row['price'], row['square_meter_price']])

