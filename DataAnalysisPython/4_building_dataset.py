import quandl 
import pandas as pd

api_key = "o44UEPHAPNE7qqzLjy-y"
df = quandl.get("FMAC/HPI_AK", authtoken=api_key, start_date="1999-01-31")
print(df.head())

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

#print(fiddy_states[0][0])

for abbv in fiddy_states[0][0][1:]:
    df = quandl.get("FMAC/HPI_"+str(abbv), authtoken=api_key, start_date="1999-01-31")
    print(df.head())

