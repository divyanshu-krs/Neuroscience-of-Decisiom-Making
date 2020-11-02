import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statistics import mean

data = pd.read_csv('Assignment_2_prp.data.2020-10-31--08-50.csv', sep=" ")


useful_data = data.loc[ ( data['status of response 1'] == 1 ) & ( data['status of response 2'] == 1 ) & ( data['blocktype'] == 2)]
#print(useful_data['SOA'])
#useful_data = data.loc[ ( data['blocktype'] == 2)]

RT_1 = list(useful_data['Response time 1']) # list of RT1
RT_2 = list(useful_data['Response time 2']) # list of RT2
SOA = list(useful_data['SOA']) # list of SOA

##
##for i in range(0, len(RT_1), 5):  
##        yield RT_1[i:i + n]
##
##for i in range(0, len(RT_2), 5):  
##        yield RT_2[i:i + n]


soa_75_1 = []
soa_75_2 = []
soa_150_1 = []
soa_150_2 = []
soa_300_1 = []
soa_300_2 = []
soa_600_1 = []
soa_600_2 = []

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

### Plot for SOA = 75 ####

# RT1
soa_75_1.sort()
p1 = np.quantile(soa_75_1, 0.2)
p2 = np.quantile(soa_75_1, 0.4)
p3 = np.quantile(soa_75_1, 0.6)
p4 = np.quantile(soa_75_1, 0.8)
p5 = np.quantile(soa_75_1, 1.0)

l_75_1 = []
l_75_1.append(p1)
l_75_1.append(p2)
l_75_1.append(p3)
l_75_1.append(p4)
l_75_1.append(p5)

# RT2
soa_75_2.sort()
q1 = np.quantile(soa_75_2, 0.2)
q2 = np.quantile(soa_75_2, 0.4)
q3 = np.quantile(soa_75_2, 0.6)
q4 = np.quantile(soa_75_2, 0.8)
q5 = np.quantile(soa_75_2, 1.0)

l_75_2 = []
l_75_2.append(q1)
l_75_2.append(q2)
l_75_2.append(q3)
l_75_2.append(q4)
l_75_2.append(q5)

### Data for SOA = 150 ####

# RT1
soa_150_1.sort()
r1 = np.quantile(soa_150_1, 0.2)
r2 = np.quantile(soa_150_1, 0.4)
r3 = np.quantile(soa_150_1, 0.6)
r4 = np.quantile(soa_150_1, 0.8)
r5 = np.quantile(soa_150_1, 1.0)

l_150_1 = []
l_150_1.append(r1)
l_150_1.append(r2)
l_150_1.append(r3)
l_150_1.append(r4)
l_150_1.append(r5)

# RT2
soa_150_2.sort()
s1 = np.quantile(soa_150_2, 0.2)
s2 = np.quantile(soa_150_2, 0.4)
s3 = np.quantile(soa_150_2, 0.6)
s4 = np.quantile(soa_150_2, 0.8)
s5 = np.quantile(soa_150_2, 1.0)

l_150_2 = []
l_150_2.append(s1)
l_150_2.append(s2)
l_150_2.append(s3)
l_150_2.append(s4)
l_150_2.append(s5)

### Data for SOA = 300 ####

# RT1
soa_300_1.sort()
t1 = np.quantile(soa_300_1, 0.2)
t2 = np.quantile(soa_300_1, 0.4)
t3 = np.quantile(soa_300_1, 0.6)
t4 = np.quantile(soa_300_1, 0.8)
t5 = np.quantile(soa_300_1, 1.0)

l_300_1 = []
l_300_1.append(t1)
l_300_1.append(t2)
l_300_1.append(t3)
l_300_1.append(t4)
l_300_1.append(t5)

# RT2
soa_300_2.sort()
u1 = np.quantile(soa_300_2, 0.2)
u2 = np.quantile(soa_300_2, 0.4)
u3 = np.quantile(soa_300_2, 0.6)
u4 = np.quantile(soa_300_2, 0.8)
u5 = np.quantile(soa_300_2, 1.0)

l_300_2 = []
l_300_2.append(u1)
l_300_2.append(u2)
l_300_2.append(u3)
l_300_2.append(u4)
l_300_2.append(u5)

### Data for SOA = 600 ####

# RT1
soa_600_1.sort()
v1 = np.quantile(soa_600_1, 0.2)
v2 = np.quantile(soa_600_1, 0.4)
v3 = np.quantile(soa_600_1, 0.6)
v4 = np.quantile(soa_600_1, 0.8)
v5 = np.quantile(soa_600_1, 1.0)

l_600_1 = []
l_600_1.append(v1)
l_600_1.append(v2)
l_600_1.append(v3)
l_600_1.append(v4)
l_600_1.append(v5)

# RT2
soa_600_2.sort()
w1 = np.quantile(soa_600_2, 0.2)
w2 = np.quantile(soa_600_2, 0.4)
w3 = np.quantile(soa_600_2, 0.6)
w4 = np.quantile(soa_600_2, 0.8)
w5 = np.quantile(soa_600_2, 1.0)

l_600_2 = []
l_600_2.append(w1)
l_600_2.append(w2)
l_600_2.append(w3)
l_600_2.append(w4)
l_600_2.append(w5)

# Plot each vector RT1 vs RT2
fig = plt.figure()
plt.plot(l_75_1,l_75_2, label = "SOA 75")
plt.plot(l_150_1,l_150_2, label='SOA 150')
plt.plot(l_300_1,l_300_2, label = "SOA 300")
plt.plot(l_600_1,l_600_2, label='SOA 600')
plt.xlabel('RT1')
plt.ylabel('RT2')
plt.legend()
plt.title('RT1 Vs RT2 For Each SOA')
caption = "Figure represents different line plot with X-axis as RT1 and Y-axis as RT2. The line in 'Blue' represnts RT1 vs RT2 for SOA=75, similary 'Orange' represents SOA=150, 'Green' represnts SOA=300 and finially 'Red' represnts SOA=600"
fig.text(0.5,0.01,caption, wrap=True, ha='center')
plt.show()
