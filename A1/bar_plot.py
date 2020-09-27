## Bar Plot ##

import matplotlib.pyplot as plot
import numpy as np
import pandas as pd

data = pd.read_csv('Data.csv')

num_spike_before_zero= []
num_spike_after_zero = []
bin_1 = 0 # (-1 to -0.9]
bin_2 = 0 # (-0.9 to -0.8]
bin_3 = 0 # (-0.8 to -0.7]
bin_4 = 0 # (-0.7 to -0.6]
bin_5 = 0 # (-0.6 to -0.5]
bin_6 = 0 # (-0.5 to -0.4]
bin_7 = 0 # (-0.4 to -0.3]
bin_8 = 0 # (-0.3 to -0.2]
bin_9 = 0 # (-0.2 to -0.1]
bin_10 = 0 # (-0.1 to 0.0]
bin_11 = 0 # (0.0 to 0.1]
bin_12 = 0 # (0.1 to 0.2]
bin_13 = 0 # (0.2 to 0.3]
bin_14 = 0 # (0.3 to 0.4]
bin_15 = 0 # (0.4 to 0.5]
bin_16 = 0 # (0.5 to 0.6]
bin_17 = 0 # (0.6 to 0.7]
bin_18 = 0 # (0.7 to 0.8]
bin_19 = 0 # (0.8 to 0.9]
bin_20 = 0 # (0.9 to 1.0]
    
for i in range(50):
    l = []
    arr_without_nan = np.array(data.iloc[i,1:])
    arr_without_nan = arr_without_nan[~np.isnan(arr_without_nan)]
    
    for j in list(arr_without_nan):
        
        if ( -1 < j <= -0.9):
            bin_1+=1
            
        elif (-0.9 < j <= -0.8):
            bin_2+=1
            
        elif (-0.8 < j <= -0.7):
            bin_3+=1
            
        elif (-0.7 < j <= -0.6):
            bin_4+=1
            
        elif (-0.6 < j <= -0.5):
            bin_5+=1
            #print('here',bin_5)
        elif (-0.5 < j <= -0.4):
            bin_6+=1
            
        elif (-0.4 < j <= -0.3):
            bin_7+=1
            
        elif (-0.3 < j <= -0.2):
            bin_8+=1
            
        elif (-0.2 < j <= -0.1):
            bin_9+=1
            
        elif (-0.1 < j <= 0.0):
            bin_10+=1
            
        elif (0.0 < j <= 0.1):
            bin_11+=1
            
        elif (0.1 < j <= 0.2):
            bin_12+=1
            
        elif (0.2 < j <= 0.3):
            bin_13+=1
            
        elif (0.3 < j <= 0.4):
            bin_14+=1
            
        elif (0.4 < j <= 0.5):
            bin_15+=1
              
        elif (0.5 < j <= 0.6):
            bin_16+=1
              
        elif (0.6 < j <= 0.7):
            bin_17+=1
              
        elif (0.7 < j <= 0.8):
            bin_18+=1
              
        elif (0.8 < j <= 0.9):
            bin_19+=1
              
        elif (0.9 < j <= 1.0):
            bin_20+=1
             

data_arr = [bin_1,bin_2,bin_3,bin_4,bin_5,bin_6,bin_7,bin_8,bin_9,bin_10,bin_11,bin_12,bin_13,bin_14,bin_15,bin_16,bin_17,bin_18,bin_19,bin_20]
print(data_arr)
x=['(-1 to -0.9]','(-0.9 to -0.8]','(-0.8 to -0.7]', '(-0.7 to -0.6]','(-0.6 to -0.5]','(-0.5 to -0.4]' , '(-0.4 to -0.3]','(-0.3 to -0.2]','(-0.2 to -0.1]','(-0.1 to 0.0]','(0.0 to 0.1]','(0.1 to 0.2]','(0.2 to 0.3]','(0.3 to 0.4]','(0.4 to 0.5]','(0.5 to 0.6]','(0.6 to 0.7]','(0.7 to 0.8]','(0.8 to 0.9]','(0.9 to 1.0]'
]
plot.bar(x,data_arr)
plot.xlabel('Time Interavals')
plot.ylabel("No of Fired spikes")
plot.title('Bar Plot')
plot.xticks(rotation=45)
plot.show()
