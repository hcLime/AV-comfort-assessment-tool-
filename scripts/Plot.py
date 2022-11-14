#!/usr/bin/python
#
#       This program produces following acceleration data plots:
#       1. lateral acceleration versus time
#       2. longitudinal acceleration versus time
#       3. lateral-longitudinal accelerations with thresholds

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime
import shapely
import shapely.geometry as geometry
import os.path
from descartes.patch import PolygonPatch


#plot lateral versus time
fig1 = plt.figure("Acc_Lateral")
ax1 = fig1.add_subplot(1,1,1)

open_path_AV = '/Users/emilc/OneDrive/Desktop/Scripts/AV_nuScenes_Data/Output'
open_path_IMU = '/Users/emilc/OneDrive/Desktop/Scripts/BerryIMU_Data'


open_name = os.path.join(open_path_AV, "BostonSeaport0103_AV_accY.txt")
#open_name = os.path.join(open_path_IMU, "Scene02-Lateral.txt")
graph_data = open(open_name,'r').read() #define input file
lines = graph_data.split('\n')
tt = []
ys = []
for line in lines:
    if len(line) > 1:
        x, y = line.split(',')
        tt.append(float(x))
        ys.append(float(y))

ax1.plot(tt, ys, '-', color="mediumblue", linewidth= 1.4)
#plt.ylim(-6, 6)
#plt.xlim(240, 260) #trim plot
plt.xlabel("Time [s]",fontsize=12, fontweight= 'bold')
plt.ylabel("Lateral Acceleration [m/s2]",fontsize=12, fontweight= 'bold')
plt.title('Lateral Acceleration versus Time',fontsize=12, fontweight= 'bold')
plt.grid()
plt.show(block=False)

#plot longitudinal versus time
fig2 = plt.figure("Acc_Longitudinal")
ax2 = fig2.add_subplot(1,1,1)

open_name = os.path.join(open_path_AV, "BostonSeaport0103_AV_accX.txt")
#open_name = os.path.join(open_path_IMU, "Scene02-Longitudinal.txt")
graph_data = open(open_name,'r').read() #define input file
lines = graph_data.split('\n')
xs = []
ys = []
for line in lines:
    if len(line) > 1:
        x, y = line.split(',')
        xs.append(float(x))
        ys.append(float(y))

ax2.plot(xs, ys, '-', color="mediumblue", linewidth= 1.4)
#plt.ylim(-6, 6)
#plt.xlim(1300, 1320) #trim plot
plt.xlabel("Time [s]",fontsize=12, fontweight= 'bold')
plt.ylabel("Longitudinal Acceleration [m/s2]",fontsize=12, fontweight= 'bold')
plt.title('Longitudinal Acceleration versus Time',fontsize=12, fontweight= 'bold')
plt.grid()
plt.show(block=False)

'''
#Jerk
#plot logitudinal versus time
fig5 = plt.figure("Jerk_Longitudinal")
ax5 = fig5.add_subplot(1,1,1)


#open_name = os.path.join(open_path_AV, "2022-08-04 20_17_lateral.txt")
open_name = os.path.join(open_path_IMU, "2022-08-13 16_01_jlongitudinal.txt")
graph_data = open(open_name,'r').read() #define input file
lines = graph_data.split('\n')
xs = []
ys = []
for line in lines:
    if len(line) > 1:
        x, y = line.split(',')
        xs.append(float(x))
        ys.append(float(y))

ax5.plot(xs, ys, '-', color="blue", markersize= 2)
#plt.ylim(-6, 6)
#plt.xlim(1300, 1320) #trim plot
plt.xlabel("Time [s]")
plt.ylabel("Longitudinal Jerk [m/s2]")
plt.grid()
plt.show(block=False)

#plot lateral versus time
fig6 = plt.figure("Jerk_Lateral")
ax6 = fig6.add_subplot(1,1,1)

#open_name = os.path.join(open_path_AV, "2022-08-04 20_17_lateral.txt")
open_name = os.path.join(open_path_IMU, "2022-08-13 16_01_jlateral.txt")
graph_data = open(open_name,'r').read() #define input file
lines = graph_data.split('\n')
xs = []
ys = []
for line in lines:
    if len(line) > 1:
        x, y = line.split(',')
        xs.append(float(x))
        ys.append(float(y))

ax6.plot(xs, ys, '-', color="blue", markersize= 4)
#plt.ylim(-6, 6)
#plt.xlim(240, 260) #trim plot
plt.xlabel("Time [s]")
plt.ylabel("Lateral Jerk [m/s2]")
plt.grid()
plt.show(block=False)
'''



##  Acceleration tresholds 
#Extremely comfortable
polygon_ecomfortable = [[-0.3,0], 
                        [0,-0.3], 
                        [0.3,0], 
                        [0,0.3]]

line = geometry.LineString(polygon_ecomfortable)
polygon_ecomfortable = geometry.Polygon(line)

#Very comfortable
polygon_vcomfortable = [[-0.6,0], 
                        [0,-0.6], 
                        [0.6,0], 
                        [0,0.6]]

line = geometry.LineString(polygon_vcomfortable)
polygon_vcomfortable = geometry.Polygon(line)

#Comfortable
polygon_comfortable = [[-0.9,0], 
                        [0,-0.9], 
                        [0.9,0], 
                        [0,0.9]]

line = geometry.LineString(polygon_comfortable)
polygon_comfortable = geometry.Polygon(line)

#Acceptable
polygon_acceptable = [[-3.6,0], 
                        [0,-1.8], 
                        [3.6,0], 
                        [0,1.3]]

line = geometry.LineString(polygon_acceptable)
polygon_acceptable = geometry.Polygon(line)

#Poor
polygon_poor = [[-4.2,0], 
                   [0,-2.4], 
                   [4.2,0], 
                   [0,1.5]]

line = geometry.LineString(polygon_poor)
polygon_poor = geometry.Polygon(line)

#Uncomfortable
polygon_uncomfortable = [[-5.6,0], 
                      [0,-5.08], 
                      [5.6,0], 
                      [0,3.07]]

line = geometry.LineString(polygon_uncomfortable)
polygon_uncomfortable = geometry.Polygon(line)

#Aggresive
polygon_aggresive = [[-5.6,0], 
                      [0,-5.08], 
                      [5.6,0], 
                      [0,3.07]]

line = geometry.LineString(polygon_aggresive)
polygon_aggresive = geometry.Polygon(line)


x1, y1 = polygon_ecomfortable.exterior.xy
x2, y2 = polygon_vcomfortable.exterior.xy
x3, y3 = polygon_comfortable.exterior.xy
x4, y4 = polygon_acceptable.exterior.xy
x5, y5 = polygon_poor.exterior.xy
x6, y6 = polygon_uncomfortable.exterior.xy


#polygon = geometry.Polygon(polygon_comfortable)


fig3 = plt.figure("X-Y acceleration")
ax3 = fig3.add_subplot()

def animate(i):
    open_name = os.path.join(open_path_AV, "BostonSeaport0103_accX-Y.txt")
    #open_name = os.path.join(open_path_IMU, "Scene03-Acc.txt")
    graph_data = open(open_name,'r').read() #define input file
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            y, x = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
            
    ax3.clear()
    
    #ax3.plot(xs, ys, '.', color="black", markersize= 2) #plot acc points
    ax3.plot(x1, y1, color="darkgreen", label='A*', linewidth= 1.8) 
    ax3.plot(x2, y2, color="green", label='A', linewidth= 1.8)
    ax3.plot(x3, y3, color="lime", label='B', linewidth= 1.8)
    ax3.plot(x4, y4, color="gold", label='C', linewidth= 1.8) 
    ax3.plot(x5, y5, color="orange", label='D', linewidth= 1.8)
    ax3.plot(x6, y6, color="red", label='E', linewidth= 1.8)
    ax3.scatter(xs,ys,marker=".",c='black',s=2**2)
    plt.ylim(-5.5, 3.5)
    plt.xlim(-6, 6)
    plt.xlabel("Lateral Acceleration [m/s2]",fontsize=12, fontweight= 'bold')
    plt.ylabel("Longitudinal Acceleration [m/s2]", fontsize=12, fontweight= 'bold')   
    plt.title('Longitudinal/Lateral Acceleration Classification',fontsize=12, fontweight= 'bold')
    plt.legend(loc='lower right')
    plt.grid()

ani = animation.FuncAnimation(fig3, animate, interval=500)
plt.show()





open_name = os.path.join(open_path_AV, "SingaporeOnenorth0061_comfort.txt")
graph_data = open(open_name,'r').read() #define input file
lines = graph_data.split('\n')
ss = []
ys = []
for line in lines:
    if len(line) > 1:
        s, y = line.split(',')
        ss.append(float(s))
        ys.append(float(y))



fig4 = plt.figure("Comfort score vs Time")
ax4 = fig4.add_subplot(1,1,1)

ax4.plot(tt, ys, '-', color="mediumblue", linewidth= 1)
plt.axhline(y=35, color='black', linestyle='-', linewidth= 0.8)
plt.axhline(y=60, color='red', linestyle='-', linewidth= 0.8)
plt.axhline(y=65, color='orange', linestyle='-', linewidth= 0.8)
plt.axhline(y=75, color='gold', linestyle='-', linewidth= 0.8)
plt.axhline(y=80, color='lime', linestyle='-', linewidth= 0.8)
plt.axhline(y=90, color='green', linestyle='-', linewidth= 0.8)
plt.axhline(y=100, color='darkgreen', linestyle='-', linewidth= 0.8)
#plt.ylim(0,100)
plt.ylim(20, 100)
plt.xlabel("Time [s]",fontsize=12, fontweight= 'bold')
plt.ylabel("Comfort Score [0-100]",fontsize=12, fontweight= 'bold')
plt.title('Comfort Score versus Time',fontsize=12, fontweight= 'bold')
plt.show()


'''
## Jerk tresholds

#Comfortable
polygon_comfortable_j = [[-0.6,0], 
                         [0,-0.6], 
                         [0.6,0], 
                         [0,0.6]]

line = geometry.LineString(polygon_comfortable_j)
polygon_comfortable_j = geometry.Polygon(line)

#Normal
polygon_normal_j = [[-0.9,0], 
                     [0,-0.9], 
                     [0.9,0], 
                     [0,0.9]]

line = geometry.LineString(polygon_normal_j)
polygon_normal_j = geometry.Polygon(line)

#Aggresive
polygon_aggresive_j = [[-2,0], 
                        [0,-2], 
                        [2,0], 
                        [0,2]]

line = geometry.LineString(polygon_aggresive_j)
polygon_aggresive_j= geometry.Polygon(line)

fig4 = plt.figure("X-Y jerk")
ax4 = fig4.add_subplot(1,1,1)

x1j, y1j = polygon_comfortable_j.exterior.xy
x2j, y2j = polygon_normal_j.exterior.xy
x3j, y3j = polygon_aggresive_j.exterior.xy

def animate2(i):
    #open_name = os.path.join(open_path_AV, "2022-08-04 20_17_lateral.txt")
    open_name = os.path.join(open_path_IMU, "2022-08-13 16_01_jerk.txt")
    graph_data = open(open_name,'r').read() #define input file
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
            
    ax4.clear()
    ax4.plot(xs, ys, '.', color="black", markersize= 2.5) #plot acc points
    plt.plot(x1j, y1j, color="green") 
    plt.plot(x2j, y2j, color="orange")
    plt.plot(x3j, y3j, color="red")
    plt.ylim(-6, 6)
    plt.xlim(-6, 6)
    plt.xlabel("Lateral Acceleration [m/s2]")
    plt.ylabel("Longitudinal Acceleration [m/s2]")
    plt.grid()

ani2 = animation.FuncAnimation(fig4, animate2, interval=500)
plt.show()
'''