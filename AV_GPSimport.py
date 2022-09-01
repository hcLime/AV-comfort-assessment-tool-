#!/usr/bin/python3
#
#       This program import AV position data.

#Convert pose data to GPS lat/long.
#from nuscenes.scripts.export_poses import main
#nusc_pos = main(dataroot='C:\\Users\\emilc\\nuscen\\Lib\\site-packages\\nuscenes', version= 'v1.0-mini', output_prefix='C:\\Users\\emilc\\nuscen\\Lib\\site-packages\\nuscenes',output_format='kml')

#coordinates conversion works for the ego_pos file. It does not include acceleration data.
#Therefore I cannot assess comfort for the coordinates. Position from the can_bus does not provide


import matplotlib.pyplot as plt
import os.path
import json

open_path='/Users/emilc/OneDrive/Desktop/Scripts/AV_nuScenes_Data'
#open GPS position data
openName = os.path.join(open_path, "nuscenes_v1.0-mini.json")
# open json file position dataset
f= open(openName)
data= json.loads(f.read())

place= data['singapore-onenorth'] #singapore-queenstown boston-seaport
scenario= place['scene-0061']

save_path='/Users/emilc/OneDrive/Desktop/Scripts/AV_nuScenes_Data/Output'
completeName5 = os.path.join(save_path, "_GPS.txt") # save long, lot position with comfort score
GPS = open(completeName5, 'a')

for x in scenario:
	lat= x['latitude']
	long= x['longitude']

	GPS.write(str(long))
	GPS.write(",")
	GPS.write(str(lat))
	GPS.write("\n")
	GPS.flush() 


