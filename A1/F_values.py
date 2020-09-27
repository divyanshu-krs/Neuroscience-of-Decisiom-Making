## Calculating F's ##
# Reference: Assignment Question

import numpy as np
import pandas as pd
import statistics 

data = pd.read_csv('Data.csv')

num_spike_before_zero= []
num_spike_after_zero = []
for i in range(50):
    l = []
    arr_without_nan = np.array(data.iloc[i,1:])
    arr_without_nan = arr_without_nan[~np.isnan(arr_without_nan)]
    
    count_before_zero = 0
    count_after_zero = 0
    for j in list(arr_without_nan):
        l.append(j)
        if (j<0):
            count_before_zero+=1
        else:
            count_after_zero+=1
   
    num_spike_before_zero.append(count_before_zero)
    num_spike_after_zero.append(count_after_zero)

## Analysis ##

#F1 before onset
mean_spike_before_all = statistics.mean(num_spike_before_zero)
deviation_spike_before_onset_each_trial = []

for i in num_spike_before_zero:
    dev = i - mean_spike_before_all
    deviation_spike_before_onset_each_trial.append(dev**2)

print("F values before onset is", (statistics.mean(deviation_spike_before_onset_each_trial) / mean_spike_before_all))

# F2 After onset
mean_spike_after_all = statistics.mean(num_spike_after_zero)
deviation_spike_after_onset_each_trial = []
for j in num_spike_after_zero:
    dev = j - mean_spike_after_all
    deviation_spike_after_onset_each_trial.append(dev**2)

print("F values after onset is", (statistics.mean(deviation_spike_after_onset_each_trial) / mean_spike_after_all))

