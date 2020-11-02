import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statistics import mean

data = pd.read_csv('Assignment_2_prp.data.2020-10-31--08-50.csv', sep=" ") # Read the data

# Selecting the data with correct responses and exluding pre-test trail data
useful_data = data.loc[ ( data['status of response 1'] == 1 ) & ( data['status of response 2'] == 1 ) & ( data['blocktype'] == 2)]
print(len(useful_data['status of response 1'])) # Correct response in both
print(len(data.loc[ (data['status of response 1'] == 1) & (data['blocktype'] == 2)]))# Correct response in Task 1
print(len(data.loc[ (data['status of response 2'] == 1) & (data['blocktype'] == 2)])) # Correct response in Task 2


