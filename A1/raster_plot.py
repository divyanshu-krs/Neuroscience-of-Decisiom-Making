## Spike Raster Plot ##
# Reference: https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.axes.Axes.eventplot.html
import matplotlib.pyplot as plot
import numpy as np
import pandas as pd
import random

data = pd.read_csv('Data.csv')
data_arr = []
for i in range(50):
    l = []
    arr_without_nan = np.array(data.iloc[i,1:])
    arr_without_nan = arr_without_nan[~np.isnan(arr_without_nan)]
    for j in arr_without_nan:
        l.append(j)
    data_arr.append(l)
    
data_arr = np.asarray(data_arr[1:])
colors1 = ['C{}'.format(i) for i in range(49)]
                        
plot.eventplot(data_arr,color=colors1)
plot.title('Raster Plot')
plot.ylabel('Trials')
plot.xlabel('Time(in second)')
plot.show()
