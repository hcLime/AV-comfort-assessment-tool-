from nuscenes.can_bus.can_bus_api import NuScenesCanBus
from nuscenes.nuscenes import NuScenes
import os.path
import json
import matplotlib.pyplot as plt

nusc = NuScenes(version='v1.0-mini', dataroot='C:\\Users\\emilc\\nuscen\\Lib\\site-packages\\nuscenes', verbose=True)
nusc.list_scenes()
#define data path
nusc_can = NuScenesCanBus(dataroot='C:\\Users\\emilc\\nuscen\\Lib\\site-packages\\nuscenes')

#pick the scene
scene_name = 'scene-0061'
nusc_can.print_all_message_stats(scene_name)

message_name = 'vehicle_monitor'
key_name = 'steering_speed'

nusc_can.plot_message_data(scene_name, message_name, key_name, dimension=0)

#problem:GPS samples are not in the same resolution as IMU. Can't assess comfort at specific timestep.
#pick parameter
#message_name = 'ms_imu'
#key_name = 'linear_accel'
#nusc_can.plot_message_data(scene_name, message_name, key_name, dimension=2) #plot
nusc_can.plot_baseline_route(scene_name)

'''
fig = plt.figure("X-Y acceleration")
ax = fig.add_subplot(1,1,1)

nusc_can.plot_baseline_route(scene_name)

open_path='/Users/emilc/OneDrive/Desktop/Scripts/AV_nuScenes_Data/Output'

open_name = os.path.join(open_path, "_GPS.txt")
open_name2 = os.path.join(open_path, "comfort.txt")

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
	[z] = y
	zs.append(float(z))

#assign marketcolor to the timestep
col=[]
for i in range(0,len(xs)):
    if zs[i]==0.0:
        col.append('g') 
    elif zs[i]==1.0:
        col.append('y')
    elif zs[i]==2.0:
        col.append('r')
    elif zs[i]==3.0:
        col.append('k') 

#plot timesteps
for i in range(len(xs)):
	ax.scatter(xs[i],ys[i],c=col[i],s=5)

plt.show()
'''