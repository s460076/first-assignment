
import pandas as pd 
df = pd.read_csv('train.tsv', sep='\t', names=['price', 'num_of_rooms', 'area', 'num_of_floors', 'address', 'desc']) 
# calculation of the average
avg_price = pd.DataFrame([round(df['price'].mean(),3)])

# saving the average to a file
avg_price.to_csv('out0.csv', index=False)
 
# dding a new column
df['square_meter_price'] = round(df['price']/df['area'],3)
# saving dataframe to a file
df_to_save = df[['num_of_rooms', 'price', 'square_meter_price']].loc[(df['num_of_rooms']>=3) & (df['square_meter_price']<df['square_meter_price'].mean())]
df_to_save.to_csv('out1.csv', index=False)