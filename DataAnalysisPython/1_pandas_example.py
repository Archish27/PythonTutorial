import pandas as pd
import datetime
import pandas_datareader as web
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2017, 8, 22)

df = web.DataReader("XOM", "yahoo", start, end)

print(df.head())

df['Adj Close'].plot()

plt.show()
