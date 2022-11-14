    #!/usr/bin/python3
#
#       This script plots GPS coordinates on the opensource map and comfort score versus time.
#       Inputs: BerryGPS position, comfort assessment

import matplotlib.pyplot as plt
import contextily as cx
import os.path

#import data
#import GPS positions
open_path_IMU='/Users/emilc/OneDrive/Desktop/Scripts/BerryIMU_Data/Output'
open_name = os.path.join(open_path_IMU, "Scene03-GPS.txt")
graph_data = open(open_name,'r').read() #define input file
dlist = graph_data.split("\n") #split timesteps
xs = []
ys = []

for x in dlist:
    [x, y] = x.split(',')
    xs.append(float(x))
    ys.append(float(y))

# comfort assessment
open_name = os.path.join(open_path_IMU, "Scene03-comfort.txt")
graph_data = open(open_name,'r').read() #define input file
dlist = graph_data.split("\n") #split timesteps
zs = []
bs = []
for x in dlist:
    [x, y] = x.split(',')
    zs.append(float(x))
    bs.append(float(y))

# obtain time
open_path_IMU='/Users/emilc/OneDrive/Desktop/Scripts/BerryIMU_Data'
open_name = os.path.join(open_path_IMU, "Scene03-Lateral.txt")
graph_data = open(open_name,'r').read() #define input file
lines = graph_data.split('\n')
ts = []
ls = []
for line in lines:
    if len(line) > 1:
        x, y = line.split(',')
        ts.append(float(x))
        ls.append(float(y))

#initialize map
west, south, east, north = (
    -2.36687,
    51.38150,
    -2.36200,
    51.38440

             )

'''
Whole route
    -2.3676,
    51.3732,
    -2.3208,
    51.3901


Scene01-parking
    -2.32540,
    51.37839,
    -2.32222,
    51.37956

Scene02-Down the hill
    -2.35450,
    51.38100,
    -2.34550,
    51.38524

Scene03- City driving
    -2.36687,
    51.38150,
    -2.36200,
    51.38440

'''

img, ext = cx.bounds2img(west,
                                     south,
                                     east,
                                     north,
                                     ll=True,
                                     source=cx.providers.Esri.WorldImagery
                                    )

warped_img, warped_ext= cx.warp_tiles(img, extent=ext, t_crs='EPSG:4326')

#Other providers:
    #Esri.WorldTopoMap
    #Esri.WorldImagery
    #OpenStreetMap.Mapnik
    #CartoDB.Voyager
    #CartoDB.Positron

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


#create figure, map plot
fig, ax = plt.subplots(1, figsize=(9, 9))
#plot timesteps
for i in range(len(xs)):
    ax.scatter(xs[i],ys[i],marker=".",c=col[i], s=10**2, edgecolors='none')
ax.imshow(warped_img, extent=warped_ext)
ax.set_ylabel("Latitude [Deg]",fontsize=12, fontweight= 'bold')
plt.title('Comfort Assessment',fontsize=12, fontweight= 'bold')
ax.set_xlabel("Longitude [Deg]",fontsize=12, fontweight= 'bold')
plt.show()

# comfort score versus time
fig2 = plt.figure("Comfort score vs Time")
ax2 = fig2.add_subplot(1,1,1)
ax2.plot(ts, bs, '-', color="blue",label='comfort score', linewidth= 1.5)
#plt.ylim(-6, 6)
#plt.xlim(1300, 1320) #trim plot
plt.title('Comfort Score versus Time',fontsize=12, fontweight= 'bold')
plt.xlabel("Time [s]",fontsize=12, fontweight= 'bold')
plt.ylabel("Comfort Score [0-100]",fontsize=12, fontweight= 'bold')
plt.axhline(y=35, color='black', label='F', linestyle='-', linewidth= 0.8)
plt.axhline(y=60, color='red', label='E', linestyle='-', linewidth= 0.8)
plt.axhline(y=65, color='orange', label='D', linestyle='-', linewidth= 0.8)
plt.axhline(y=75, color='gold', label='C', linestyle='-', linewidth= 0.8)
plt.axhline(y=80, color='lime', label='B', linestyle='-', linewidth= 0.8)
plt.axhline(y=90, color='green', label='A', linestyle='-', linewidth= 0.8)
plt.axhline(y=100, color='darkgreen', label='A*', linestyle='-', linewidth= 0.8)
#plt.legend(loc='lower right')
plt.ylim(20, 100)
plt.show()