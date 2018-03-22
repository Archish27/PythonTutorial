import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,53,34,45,64,33],
             'Bounce_Rate' : [65,72,62,64,54,66]}

df = pd.DataFrame(web_stats)
##df2 = df.set_index('Day')
##print(df2)

df.set_index('Day',inplace =True)

print(df)


print(df.Visitors)

print(df[['Visitors','Bounce_Rate']])

print(df.Visitors.tolist())

print(np.array(df[['Visitors','Bounce_Rate']]))

df2= pd.DataFrame(np.array(df[['Visitors','Bounce_Rate']]))

print(df2)
