import quandl 
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = "o44UEPHAPNE7qqzLjy-y"

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]

#print(fiddy_states[0][0])
def grab_initial_state_data():
    main_df = pd.DataFrame()

    for abbv in state_list():
        df = quandl.get("FMAC/HPI_"+str(abbv), authtoken=api_key, start_date="1999-01-31")
        df.rename(columns={'Value' : str(abbv)},inplace = True)
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0
        
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df,lsuffix = str(abbv))
       # print(main_df.head())
        pickle_out = open('fiddy_states4.pickle','wb')
        pickle.dump(main_df,pickle_out)
        pickle_out.close();

def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df.rename(columns = {'Value':'United States'},inplace = True)
    df["United States"] = (df["United States"] - df["United States"][0]) / df["United States"][0] * 100.0
    return df
#grab_initial_state_data()

fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

HPI_data = pd.read_pickle('fiddy_states4.pickle')

HPI_data['TXone_yr'] = HPI_data['TX'].resample('A',how='mean')
#Default is mean in how attribute
#Look for resampling rules, change 1st args respectively

print(HPI_data[['TX','TXone_yr']])

#To deal with handling missing data you probably do 2 things:
#1. You keep it as it / Ignore it
#2. You remove it
#3. Replace with certain data

#This represents to remove data --> Default = any
HPI_data.dropna(inplace=True)

#Removes only when all columns has NaN
#HPI_data.dropna(how='all',inplace=True)



#HPI_data.fillna(method='bfill',inplace=True)
#ffill -> Forward Fill
#bfill -> Backward Fill

#Filling NaN
#HPI_data.fillna(value=-99999,limit=10,inplace=True)

print(HPI_data[['TX','TXone_yr']])
#print(HPI_data.isnull().values.sum())

HPI_data[['TX','TXone_yr']].plot(ax = ax1)

plt.legend(loc=4)
plt.show()




