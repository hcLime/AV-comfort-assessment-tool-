#!/usr/bin/python3
#       This program was developed to assess occupant's comfort within the AV.
#       This program uses nuScenes opensource AV datasets. 

import matplotlib.pyplot as plt
import shapely
import shapely.geometry as geometry
import json
import numpy
from scipy.signal import lfilter
import os.path
import time


def save(u, score):

    comfort.write(str(u))
    comfort.write(",")
    comfort.write(str(score))
    comfort.write("\n")
    comfort.flush()

#Comfort assessment function
def comfortAssess():
    status1 = polygon_ecomfortable.contains(acceleration)
    status2 = polygon_vcomfortable.contains(acceleration)
    status3 = polygon_comfortable.contains(acceleration)
    status4 = polygon_acceptable.contains(acceleration)
    status5 = polygon_poor.contains(acceleration)
    status6 = polygon_uncomfortable.contains(acceleration)
    
    status_j1 = polygon_ecomfortable_j.contains(jerk)
    status_j2 = polygon_vcomfortable_j.contains(jerk)
    status_j3 = polygon_comfortable_j.contains(jerk)
    status_j4 = polygon_acceptable_j.contains(jerk)
    status_j5 = polygon_poor_j.contains(jerk)
    status_j6 = polygon_uncomfortable_j.contains(jerk)

    cumulativeAcc= (abs(Point_X)+abs(Point_Y))

    if status1 == True and status_j1 == True:
        print('Extremely comfortable')
        score = (100)
        cumulative = (0.6)
        points = (10)
        calc= (cumulativeAcc/cumulative)
        score= (score-(points*calc))
        print(score)
        save(0, score)

    else:
        if status2 == True and status_j2 == True:
            print('Very comfortable')
            score = (90)
            cumulative = (1.2)
            points = (10)
            calc= (cumulativeAcc/cumulative)
            score= (score-(points*calc))
            print(score)
            save(1, score)

        else:
            if status3 == True and status_j3 == True:
                print('Comfortable')
                score = (80)
                cumulative = (1.8)
                points = (5)
                calc= (cumulativeAcc/cumulative)
                score= (score-(points*calc))
                print(score)
                save(2, score)
            else:
                if status4 == True and status_j4 == True:
                    print('Acceptable')
                    score = (75)
                    points = (10)
                    if Point_Y < 0:
                        cumulative = (5.5)
                        calc = (cumulativeAcc/cumulative)
                        score = (score-(points*calc))
                        print(score)
                    else:
                        cumulative = (5)
                        calc= (cumulativeAcc/cumulative)
                        score= (score-(points*calc))
                        print(score)
                    save(3, score)
                else:
                    if status5 == True and status_j5 == True:
                        print('Poor')
                        score = (65)
                        points = (5)
                        if Point_Y < 0:
                            cumulative = (6.7)
                            calc = (cumulativeAcc/cumulative)
                            score = (score-(points*calc))
                            print(score)
                        else:
                            cumulative = (5.8)
                            calc= (cumulativeAcc/cumulative)
                            score= (score-(points*calc))
                            print(score)
                        save(4, score)
                    else:
                        if status6 == True and status_j6 == True:
                            print('Uncomfortable')
                            score = (60)
                            points = (25)
                            if Point_Y < 0:
                                cumulative = (10.7)
                                calc = (cumulativeAcc/cumulative)
                                score = (score-(points*calc))
                                print(score)
                            else:
                                cumulative = (8.7)
                                calc= (cumulativeAcc/cumulative)
                                score= (score-(points*calc))
                                print(score)
                            save(5, score)
                        else:
                            print('Extremely uncomfortable')
                            score = (35)
                            cumulative = (15.2)
                            points = (35)
                            calc= (cumulativeAcc/cumulative)
                            score= (score-(points*calc))
                            print(score)
                            save(6, score)
    return

#import data 
#IMU data sampled at 100Hz
open_path='/Users/emilc/OneDrive/Desktop/Scripts/AV_nuScenes_Data'
openName1 = os.path.join(open_path, "scene-0916_ms_imu.json") # accelerations
# open json file IMU dataset
with open(openName1, 'r') as json_file:
    json_load1 = json.load(json_file)

#open GPS position data (can bus position data / 50Hz) 
openName2 = os.path.join(open_path, "scene-0916_pose.json") #position
# open json file position dataset
with open(openName2, 'r') as json_file:
    json_load2 = json.load(json_file)


# create output datafiles
save_path='/Users/emilc/OneDrive/Desktop/Scripts/AV_nuScenes_Data/Output'
completeName1 = os.path.join(save_path, "AV_accX.txt")
completeName2 = os.path.join(save_path, "AV_accY.txt")
completeName3 = os.path.join(save_path, "AV_accX-Y.txt")
completeName4 = os.path.join(save_path, "AV_jerk.txt")
completeName5 = os.path.join(save_path, "1_GPS.txt") # save long, lot position with comfort score
completeName6 = os.path.join(save_path, "comfort.txt")

lateral = open(completeName1,'a')
longitudinal = open(completeName2,'a')
acc = open(completeName3,'a')
j = open(completeName4,'a')
GPS = open(completeName5, 'a')
comfort= open(completeName6, 'a')




#initilise 
time1= 1532402927649034
Tprev= 0
Point_X_j = 0
Point_Y_j = 0
Point_X_prev = 0
Point_Y_prev = 0


for y in json_load2:
    values2 = y['pos'] #accelerations
    lat = values2[0]
    long = values2[1]
    
    GPS.write(str(long))
    GPS.write(",")
    GPS.write(str(lat))
    GPS.write("\n")
    GPS.write(str(0))
    GPS.write(",")
    GPS.write(str(0))
    GPS.write("\n")
    GPS.flush() 
    


for x in json_load1:

    #search for data within input dataset
    values1 = x['linear_accel'] #accelerations
    time = x['utime'] #uniform time zone time
    lat= x
    Tcurrent = (time - time1)/1000000 #convert to seconds
    dt= Tcurrent-Tprev #timestep
    Point_X = (values1[0]) #choose X accelerations
    Point_Y = (values1[1]) #choose Y accelerations

    

    Point_X_j= 0 #Lateral jerk
    Point_Y_j= 0 #Longitudinal jerk

    #assign current timestep to previous timestep
    Tprev = Tcurrent
    
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
    acceleration = geometry.Point(Point_X, Point_Y)
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

    point= geometry.Point([Point_X, Point_Y])


    ## Jerk tresholds
    #Extremely comfortable
    polygon_ecomfortable_j = [[-0.2,0], 
                             [0,-0.2], 
                             [0.2,0], 
                             [0,0.2]]

    line = geometry.LineString(polygon_ecomfortable_j)
    polygon_ecomfortable_j = geometry.Polygon(line)

    #Very comfortable
    polygon_vcomfortable_j = [[-0.4,0], 
                             [0,-0.4], 
                             [0.4,0], 
                             [0,0.4]]

    line = geometry.LineString(polygon_vcomfortable_j)
    polygon_vcomfortable_j = geometry.Polygon(line)

    #Comfortable
    polygon_comfortable_j = [[-0.6,0], 
                             [0,-0.6], 
                             [0.6,0], 
                             [0,0.6]]

    line = geometry.LineString(polygon_comfortable_j)
    jerk = geometry.Point(Point_X_j, Point_Y_j)
    polygon_comfortable_j = geometry.Polygon(line)

    #Acceptable
    polygon_acceptable_j = [[-0.8,0], 
                         [0,-0.8], 
                         [0.8,0], 
                         [0,0.8]]

    line = geometry.LineString(polygon_acceptable_j)
    polygon_acceptable_j = geometry.Polygon(line)

    #Poor
    polygon_poor_j = [[-0.95,0], 
                         [0,-0.95], 
                         [0.95,0], 
                         [0,0.95]]

    line = geometry.LineString(polygon_poor_j)
    polygon_poor_j = geometry.Polygon(line)

    #Uncomfortable
    polygon_uncomfortable_j = [[-2,0], 
                            [0,-2], 
                            [2,0], 
                            [0,2]]

    line = geometry.LineString(polygon_uncomfortable_j)
    polygon_uncomfortable_j= geometry.Polygon(line)

    #assess comfort
    comfortAssess()

    #save data to file

    lateral.write(str(Tcurrent))
    lateral.write(",")
    lateral.write(str(Point_X))
    lateral.write("\n")
    lateral.flush()

    longitudinal.write(str(Tcurrent))
    longitudinal.write(",")
    longitudinal.write(str(Point_Y))
    longitudinal.write("\n")
    longitudinal.flush()

    acc.write(str(Point_X))
    acc.write(",")
    acc.write(str(Point_Y))
    acc.write("\n")
    acc.flush()
        
    j.write(str(Point_X_j))
    j.write(",")
    j.write(str(Point_Y_j))
    j.write("\n")
    j.flush()






