#!/usr/bin/python3
#
#       This script produces other plots.
#       Input: BerryIMU data (speed, altitude, time)
#		Outputplots:
#					- Speed vs Time
#					- Altitude vs Time

import json
import matplotlib.pyplot as plt
import os.path
import pandas as pd


open_path='/Users/emilc/OneDrive/Desktop/Scripts/BerryIMU_Data'
open_name1 = os.path.join(open_path, "Scene03-Speed.txt") #open speed file
open_name2 = os.path.join(open_path, "Scene03-Altitude.txt") #open altitude file
graph_data = open(open_name1,'r').read() #define input file

dlist = graph_data.split("\n") #split timesteps
xs = []
ys = []


for x in dlist:
	[x, y] = x.split(',')
	if y=='nan':
		print('ok')
	else:
		xs.append(float(x))
		ys.append((float(y)*3.6)) #m/s to km/h


fig1 = plt.figure('Speed vs Time')
ax = plt.subplot()
ax.plot(xs, ys,'-', color="royalblue", linewidth= 2)
ax.set_ylabel("Velocity [km/h]",fontsize=12, fontweight= 'bold')
ax.set_xlabel("Time [s]",fontsize=12, fontweight= 'bold')
ax.grid()
plt.title('Velocity versus Time',fontsize=12, fontweight= 'bold')
plt.show()

graph_data2 = open(open_name2,'r').read() #define input file
dlist2 = graph_data2.split("\n") #split timesteps
xs = []
ys = []


for x in dlist2:
	[x, y] = x.split(',')
	if y=='nan':
		print('ok')
	else:
		xs.append(float(x))
		ys.append(float(y))

fig2 = plt.figure('Altitude vs Time')
ax = plt.subplot()
ax.plot(xs, ys,'-', color="indianred", linewidth= 2)
ax.set_ylabel("Altitude [m]",fontsize=12, fontweight= 'bold')
ax.set_xlabel("Time [s]",fontsize=12, fontweight= 'bold')
plt.title('Altitude versus Time',fontsize=12, fontweight= 'bold')
ax.grid()
plt.show()