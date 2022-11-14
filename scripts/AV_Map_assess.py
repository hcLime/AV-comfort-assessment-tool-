#!/usr/bin/python3
#
#       This program plots AV drive GPS coordinates on the opensource map.

import matplotlib.pyplot as plt
import os.path
import json
import contextily as cx
import os.path


open_path='/Users/emilc/OneDrive/Desktop/Scripts/AV_nuScenes_Data/Output'
open_name = os.path.join(open_path, "SingaporeOnenorth0061_GPS_canbus.txt") #open GPS file
open_name2 = os.path.join(open_path, "SingaporeOnenorth0061_comfort.txt")
graph_data = open(open_name,'r').read() #define input file
graph_data2 = open(open_name2,'r').read()

dlist = graph_data.split("\n") #split timesteps
dlist2= graph_data2.split("\n")
xs = []
ys = []
zs = []

for x in dlist:
    [y, x] = x.split(',')
    xs.append(float(x))
    ys.append(float(y))

for y in dlist2:
    [z, b] = y.split(',')
    zs.append(float(z))


#assign marketcolor to the timestep
col=[]
for i in range(0,len(xs)):
    if zs[i]==0.0:
        col.append('darkgreen') 
    elif zs[i]==1.0:
        col.append('green')
    elif zs[i]==2.0:
        col.append('lime')
    elif zs[i]==3.0:
        col.append('gold')
    elif zs[i]==4.0:
        col.append('orange')
    elif zs[i]==5.0:
        col.append('red')
    elif zs[i]==6.0:
        col.append('black')


fig = plt.figure("X-Y acceleration")
ax = fig.add_subplot(1,1,1)

#plot timesteps
for i in range(len(xs)):
    ax.scatter(xs[i],ys[i],c=col[i],s=4**2)
#plt.ylim(1770, 1840) #70 100 130
#plt.xlim(640, 730) #90 110 190
#plt.ylim(1560, 1660) #70 100 130
#plt.xlim(580, 710) #90 110 190
plt.ylim(1070, 1200) #70 100 130
plt.xlim(320, 490) #90 110 190
plt.xlabel("X-Position [m]", fontsize=12, fontweight= 'bold')
plt.ylabel("Y-Position [m]", fontsize=12, fontweight= 'bold')
plt.title('Comfort Assessment',fontsize=12, fontweight= 'bold')
plt.grid()
plt.show()
