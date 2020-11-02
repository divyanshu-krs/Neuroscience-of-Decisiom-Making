import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statistics import mean

# Load whole data
data = pd.read_csv('Assignment_2_prp.data.2020-10-31--08-50.csv', sep=" ")


# Required data for the analysis
useful_data = data.loc[ ( data['status of response 1'] == 1 ) & ( data['status of response 2'] == 1 ) & ( data['blocktype'] == 2)]
#print(useful_data['SOA'])

RT_1 = list(useful_data['Response time 1']) # list of RT1
RT_2 = list(useful_data['Response time 2']) # list of RT2
SOA = list(useful_data['SOA']) # list of SOA

# Individual lists to store each soa for each task (RT1 and RT2)
soa_75_1 = []
soa_75_2 = []
soa_150_1 = []
soa_150_2 = []
soa_300_1 = []
soa_300_2 = []
soa_600_1 = []
soa_600_2 = []

# Run a loop and classify all SOA based status of response into specific lists
for i in range(len(SOA)):

    if (SOA[i] == 75):
        soa_75_1.append(RT_1[i])
        soa_75_2.append(RT_2[i])
        
    elif (SOA[i] == 150):
        soa_150_1.append(RT_1[i])
        soa_150_2.append(RT_2[i])

    elif (SOA[i] == 300):
        soa_300_1.append(RT_1[i])
        soa_300_2.append(RT_2[i])
        
    elif (SOA[i] == 600):
        soa_600_1.append(RT_1[i])
        soa_600_2.append(RT_2[i])


# list to store mean of each RT
mean_RT_1 = []
mean_RT_2 = []


mean_RT_1.append(mean(soa_75_1))
mean_RT_1.append(mean(soa_150_1))
mean_RT_1.append(mean(soa_300_1))
mean_RT_1.append(mean(soa_600_1))

mean_RT_2.append(mean(soa_75_2))
mean_RT_2.append(mean(soa_150_2))
mean_RT_2.append(mean(soa_300_2))
mean_RT_2.append(mean(soa_600_2))

x = ['75','150','300','600'] # list of only possible SOA

# Plotting the figure
fig = plt.figure()
plt.plot(x,mean_RT_1, label='RT 1')
plt.plot(x,mean_RT_2, label='RT 2')
plt.legend()
plt.xlabel('Stimulus Onset Asynchronies (SOA) in ms') # Label for x axis
plt.ylabel('Mean Response Time in ms') # Label for y axis
plt.title('Mean Response Time Vs Stimulus Onset Asynchronies (SOA)') # Plot title
caption = "The figure represent Four possible SOA's i.e 75, 150, 300, 600 on the X-axis and Mean response time for various RT's i.e RT1 and RT2 on the Y-axis. The two plot lines represent a line plot connecting four mean point of each RT1 (colored - Blue) and RT2 (colored - Orange) for each SOA."
fig.text(0.5, 0.01, caption, wrap=True, ha="center", fontsize=10)
plt.show()
