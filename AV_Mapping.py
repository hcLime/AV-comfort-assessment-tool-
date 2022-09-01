#!/usr/bin/python3
#
#       This program plots AV drive GPS coordinates on the opensource map.

import matplotlib.pyplot as plt
import os.path
import json
import contextily as cx
import os.path


#initialize map
west, south, east, north = (
    -71.0857,
    42.3202,
    -70.9839,
    42.3643
             )

img, ext = cx.bounds2img(west,
                                     south,
                                     east,
                                     north,
                                     ll=True,
                                     source=cx.providers.OpenStreetMap.Mapnik
                                    )

warped_img, warped_ext= cx.warp_tiles(img, extent=ext, t_crs='EPSG:4326')

open_path='/Users/emilc/OneDrive/Desktop/Scripts/AV_nuScenes_Data/Output'
open_name = os.path.join(open_path, "_GPS.txt") #open GPS file
#open_name2 = os.path.join(open_path, "comfort.txt")
graph_data = open(open_name,'r').read() #define input file
#graph_data2 = open(open_name2,'r').read()

dlist = graph_data.split("\n") #split timesteps
#dlist2= graph_data2.split("\n")
xs = []
ys = []
#zs = []

for x in dlist:
	[x, y] = x.split(',')
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


fig = plt.figure("X-Y acceleration")
ax = fig.add_subplot(1,1,1)

#plot timesteps
for i in range(len(xs)):
	ax.scatter(xs[i],ys[i],c=col[i],s=5)

ax.scatter(xs, ys,s=5)
ax.imshow(warped_img, extent=warped_ext)
plt.show()









'''
some spares
from nuscenes.nuscenes import NuScenes
nusc = NuScenes(version='v1.0-mini', verbose=False)

# Render ego poses.
nusc_map_bos = NuScenesMap(dataroot='C:\\Users\\emilc\\nuscen\\Lib\\site-packages\\nuscenes', map_name='boston-seaport')
ego_poses = nusc_map_bos.render_egoposes_on_fancy_map(nusc, scene_tokens=[nusc.scene[3]['token']], verbose=False)
plt.show()


'''

#from nuscenes.map_expansion.map_api import NuScenesMap
#from nuscenes.map_expansion import arcline_path_utils
#from nuscenes.map_expansion.bitmap import BitMap
'''
from nuscenes.can_bus.can_bus_api import NuScenesCanBus

nusc_can = NuScenesCanBus(dataroot='C:\\Users\\emilc\\nuscen\\Lib\\site-packages\\nuscenes')

scene_name = 'scene-0001'
nusc_can.print_all_message_stats(scene_name)
'''

#nusc_map = NuScenesMap(dataroot='C:\\Users\\emilc\\nuscen\\Lib\\site-packages\\nuscenes', map_name='boston-seaport')


#bitmap = BitMap(nusc_map.dataroot, nusc_map.map_name, 'basemap')
#fig, ax = nusc_map.render_layers(['lane'], figsize=1, bitmap=bitmap)

