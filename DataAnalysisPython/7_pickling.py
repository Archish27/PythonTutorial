import quandl 
import pandas as pd
import pickle

api_key = "o44UEPHAPNE7qqzLjy-y"

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]

#print(fiddy_states[0][0])
def grab_initial_state_data():
    main_df = pd.DataFrame()

    for abbv in state_list():
        df = quandl.get("FMAC/HPI_"+str(abbv), authtoken=api_key, start_date="1999-01-31")
        
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df,lsuffix = '_caller')
 
        pickle_out = open('fiddy_states.pickle','wb')
        pickle.dump(main_df,pickle_out)
        pickle_out.close();

grab_initial_state_data() 


#Two ways to pickle
#From pickle library
#pandas to pickle from
#pickle serializes and saves the byte stream basically the byte code
#then you can load it back in & it has all of the attributes so
#if you pickle a data frame when you load that data frame back in
#you can still do you know the DF head and all that kind of stuffs
# In other words you can save & load any kind of objects or files back again    
