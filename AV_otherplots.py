#!/usr/bin/python3
#
#       This script produces velocity and yaw rate plots

import matplotlib.pyplot as plt
import numpy as np
import os.path
import json


open_path='/Users/emilc/OneDrive/Desktop/Scripts/AV_nuScenes_Data'
openName = os.path.join(open_path, "scene-0061_vehicle_monitor.json")
# open json file IMU dataset
with open(openName, 'r') as json_file:
    json_load = json.load(json_file)

speeds= []
steerang= []
tim= []
time= []
yaw= []

for y in json_load:
	steps= y['utime']
	tim.append(float(steps))

t1= tim[0]

for x in json_load:
	speed = x['vehicle_speed']
	steering = x['steering']
	timestep = x['utime']
	brake= x['brake']
	yaww= x['yaw_rate']

	speeds.append(float(speed))
	steerang.append(float(steering))
	time.append(float((timestep-t1)/1000000))
	yaw.append(float(yaww))


fig1 = plt.figure('Velocity & Steering vs Time')
ax = plt.subplot()
ax2 = ax.twinx()
ax.plot(time, speeds,'-', color="indianred", linewidth= 2.5)
ax2.plot(time, steerang,'-', color="royalblue", linewidth= 2.5)
ax.set_ylabel("Velocity [km/h]",fontsize=12, fontweight= 'bold', color='indianred')
ax2.set_ylabel("Steering [Deg]",fontsize=12, fontweight= 'bold', color='royalblue')
ax.set_xlabel("Time [s]",fontsize=12, fontweight= 'bold')
ax.grid(axis='x')
plt.title('Velocity & Steering versus Time',fontsize=12, fontweight= 'bold')
plt.show()

fig2 = plt.figure('Yaw rate vs Time')
ax = plt.subplot()
ax.plot(time, yaw,'-', color="indianred", linewidth= 2.5)

ax.set_ylabel("Yaw Rate [Des/s]",fontsize=12, fontweight= 'bold', color='indianred')
ax.set_xlabel("Time [s]",fontsize=12, fontweight= 'bold')
ax.grid()
plt.title('Yaw rate versus Time',fontsize=12, fontweight= 'bold')
plt.show()


