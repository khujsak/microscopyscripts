"""
Extracts Mean and SD from SIRT log files output from IMOD and plots
Aids Convergance Checks
"""

import matplotlib.pyplot as plt


data = open('tilt_sirt-finish.log').read()

l=[]
for t in data.split():
    try:
        l.append(float(t))
    except ValueError:
        pass

mean=[]    

for index in range(0,int(len(l)/3)):
    i=index*3
    mean.append(l[i+1])
sd=[]
for index in range(0,int(len(l)/3)):
    i=index*3
    sd.append(l[i+2])
    
mean, = plt.plot(mean, label='Mean Error')
sd, = plt.plot(sd, label='SD of Error')
plt.legend(handles=[mean, sd])
