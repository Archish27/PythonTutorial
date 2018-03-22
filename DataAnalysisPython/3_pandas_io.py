import pandas as pd

df = pd.read_csv("ZILLOW-Z77006_ZRIFAH.csv")
print(df.head())
df.set_index('Date', inplace = True)
df.to_csv('new_csv_1.csv')

df = pd.read_csv('new_csv_1.csv')
print(df.head())

df = pd.read_csv('new_csv_1.csv', index_col=0)
print(df.head())

#Rename column
df.columns = ['Austin_HPI']
print(df.head())

#Saving to CSV
df.to_csv('new_csv_2.csv')

df.to_csv('new_csv_3.csv',header=False)

#Index = Date & explicilty you are reading 
df = pd.read_csv('new_csv_3.csv', names=['Date','Austine_HPI'],index_col=0)
print(df.head())

df.to_html('example.html')

df = pd.read_csv('new_csv_3.csv', names=['Date','Austine_HPI'])
print(df.head())

#Anotherway to rename column
df.rename(columns={'Austine_HPI':'77006_HPI'},inplace=True)
print(df.head())










