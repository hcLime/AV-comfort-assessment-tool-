#!/usr/bin/python3
#       This program presents an attempt to the acceleration data filtering.

import matplotlib.pyplot as plt
from scipy.signal import lfilter
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime
import shapely
import shapely.geometry as geometry

#First plot
#input data
graph_data = open("Scene02-Lateral.txt",'r').read()
lines = graph_data.split('\n')
xs = []
ys = []
for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))


#apply lfilter
n = 15  # the larger n is, the smoother curve will be
b = [1.0 / n] * n
a = 1
yy = lfilter(b,a,ys) #lfilter
fig1 = plt.figure("lateral")
plt.plot(xs, ys, color= 'royalblue')
plt.plot(xs, yy, color= 'red')  # smooth by filter
plt.ylim(-4, 4)
plt.xlabel("Time [s]")
plt.ylabel("Lateral Acceleration [m/s2]")
plt.grid()
plt.show()

#save = open("filtered.txt", 'a')



#Savitzky-Golay filter
'''
from scipy.signal import savgol_filter
window_len = 10
polyorder = 1
yy = savgol_filter(ys, window_len, polyorder)
plt.plot(xs, ys, color= 'royalblue')
plt.plot(xs, yy, color= 'red')  # smooth by filter
plt.ylim(-4, 4)
plt.xlabel("Time [s]")
plt.ylabel("Lateral Acceleration [m/s2]")
plt.grid()
plt.show()

def filt():
    ACC_LPF_FACTOR = 0.4
    ###############################################
    #### Apply low pass filter ####
    ###############################################
    ACCx =  ACCx  * ACC_LPF_FACTOR + oldXAccRawValue*(1 - ACC_LPF_FACTOR);
    ACCy =  ACCy  * ACC_LPF_FACTOR + oldYAccRawValue*(1 - ACC_LPF_FACTOR);

    oldXAccRawValue = ACCx
    oldYAccRawValue = ACCy

int(xs)
ACC_LPF_FACTOR = 0.4
for i in ys:
    ACCx= xs[i]
    ACCy= ys[i]
    ACCx =  ACCx  * ACC_LPF_FACTOR + oldXAccRawValue*(1 - ACC_LPF_FACTOR);
    ACCy =  ACCy  * ACC_LPF_FACTOR + oldYAccRawValue*(1 - ACC_LPF_FACTOR);
    oldXAccRawValue = ACCx
    oldYAccRawValue = ACCy


'''

'''

#save.write(str(w))


#Second plot
##  Acceleration tresholds 
#Comfortable
polygon_comfortable = [[-0.9,0], 
                        [0,-0.9], 
                        [0.9,0], 
                        [0,0.9]]

line = geometry.LineString(polygon_comfortable)
polygon_comfortable = geometry.Polygon(line)

#Normal
polygon_normal = [[-4,0], 
                   [0,-2], 
                   [4,0], 
                   [0,1.47]]

line = geometry.LineString(polygon_normal)
polygon_normal = geometry.Polygon(line)

#Aggresive
polygon_aggresive = [[-5.6,0], 
                      [0,-5.08], 
                      [5.6,0], 
                      [0,3.07]]

line = geometry.LineString(polygon_aggresive)
polygon_aggresive = geometry.Polygon(line)
#style.use('fivethirtyeight')

x1, y1 = polygon_comfortable.exterior.xy
x2, y2 = polygon_normal.exterior.xy
x3, y3 = polygon_aggresive.exterior.xy

graph_data = open("2022-07-31 18_59_acc.txt",'r').read()
lines = graph_data.split('\n')
xs = []
ys = []
for line in lines:
    if len(line) > 1:
        x, y = line.split(',')
        xs.append(float(x))
        ys.append(float(y))
            
#apply lfilter
n = 10  # the larger n is, the smoother curve will be
b = [1.0 / n] * n
a = 1
yy = lfilter(b,a,ys) #lfilter longitudinal
xx = lfilter(b,a,xs) #lfilter lateral


fig2 = plt.figure("acc")
#plt.plot(xx, yy, '.', color="black", markersize= 3)  # smooth by filter
plt.plot(xs, ys, '.', color="black", markersize= 3)
plt.plot(x1, y1, color="green") 
plt.plot(x2, y2, color="orange")
plt.plot(x3, y3, color="red")
plt.xlabel("Lateral Acceleration [m/s2]")
plt.ylabel("Longitudinal Acceleration [m/s2]")
plt.grid()
plt.show()


ACC_LPF_FACTOR = 0.4    # Low pass filter constant for accelerometer


    ###############################################
    #### Apply low pass filter ####
    ###############################################


    ACCx =  ACCx  * ACC_LPF_FACTOR + oldXAccRawValue*(1 - ACC_LPF_FACTOR);
    ACCy =  ACCy  * ACC_LPF_FACTOR + oldYAccRawValue*(1 - ACC_LPF_FACTOR);
    ACCz =  ACCz  * ACC_LPF_FACTOR + oldZAccRawValue*(1 - ACC_LPF_FACTOR);


    oldXAccRawValue = ACCx
    oldYAccRawValue = ACCy
    oldZAccRawValue = ACCz
'''