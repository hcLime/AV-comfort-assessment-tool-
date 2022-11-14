#!/usr/bin/python
#
#       This program assess the vehicle comfort level based on the acceleration input.
#

import time
import IMU
import sys
import shapely.geometry as geometry
import matplotlib.pyplot as plt
from datetime import datetime
import os.path

#Comfort assessment 
def comfortAssess():

    status1 = polygon_comfortable.contains(acceleration)
    status2 = polygon_normal.contains(acceleration)
    status3 = polygon_aggresive.contains(acceleration)

    status_j1 = polygon_comfortable_j.contains(jerk)
    status_j2 = polygon_normal_j.contains(jerk)
    status_j3 = polygon_aggresive_j.contains(jerk)

    if status1 == True and status_j1 == True:
        comf = print('comfortable')
    else:
        if status2 == True and status_j2 == True:
            comf = print('normal')
        else:
            if status3 == True and status_j3 == True:
                comf = print('aggresive')
            else:
                comf = print('extreme')     
    return comf

#Plot acceleration tresholds
def treshplot():
    #Plotting tresholds
    x1, y1 = polygon_comfortable.exterior.xy
    x2, y2 = polygon_normal.exterior.xy
    x3, y3 = polygon_aggresive.exterior.xy


    plt.figure("Acceleration Tresholds")
    plt.plot(x1, y1) 
    plt.plot(x2, y2)
    plt.plot(x3, y3)
    plt.xlabel("Lateral Acceleration [m/s2]")
    plt.ylabel("Longitudinal Acceleration [m/s2]")
    plt.grid()
    plt.pause(0.05)
    plt.show()
    

IMU.detectIMU()     #Detect if BerryIMU is connected.
if(IMU.BerryIMUversion == 99):
    print(" No BerryIMU found... exiting ")
    sys.exit()
IMU.initIMU()       #Initialise the accelerometer, gyroscope and compass

#initialise
t = time.time()
yGcurrent= 0
xGcurrent= 0
Tprev=0

#Data logging files
current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M')
file_name = str(current_datetime)
save_path='/home/chodowi/BerryIMU/python-BerryIMU-measure-G/Data log'

completeName1 = os.path.join(save_path, file_name+"_lateral.txt")
completeName2 = os.path.join(save_path, file_name+"_longitudinal.txt")
completeName3 = os.path.join(save_path, file_name+"_acc.txt")
completeName4 = os.path.join(save_path, file_name+"_jerk.txt")
completeName5 = os.path.join(save_path, file_name+"_utime.txt")

lateral = open(completeName1, 'a')
longitudinal = open(completeName2, 'a')
acc = open(completeName3, 'a')
j = open(completeName4, 'a')
time1 = open(completeName5, 'a')


while True:
    
    Tcurrent= time.time()-t
    time2= time.time()
    dt= Tcurrent-Tprev #timestep
    print(time2)

    #Read the accelerometer,gyroscope and magnetometer values
    ACCx = IMU.readACCx()
    ACCy = IMU.readACCy()
    ACCz = IMU.readACCz()
    #yG = (ACCx * 0.244)/1000
    #xG = (ACCy * 0.244)/1000
    #zG = (ACCz * 0.244)/1000
    
    # get more accurate G value / read more about accuaracy of IMU sensor
    # Macro for mg per LSB at +/- 2g sensitivity (1 LSB = 0.000244mg)
    # Macro for mg per LSB at +/- 4g sensitivity (1 LSB = 0.000488mg)
    # Macro for mg per LSB at +/- 8g sensitivity (1 LSB = 0.000976mg)
    xG =  9.80665*(ACCx * 0.000244)
    yG =  9.80665*(ACCy * 0.000244)
    zG =  9.80665*(ACCz * 0.000244)- 9.80665
    #print("##### X = %fG  ##### Y =   %fG  ##### Z =  %fG  #####" % ( ACCy, ACCx, ACCz)) #G values
    
    Point_X_j= (xG-xGcurrent)/dt #Lateral jerk
    Point_Y_j= (yG-yGcurrent)/dt #Longitudinal jerk

    
    ##  Acceleration tresholds 
    #Comfortable
    polygon_comfortable = [[-0.9,0], 
                            [0,-0.9], 
                            [0.9,0], 
                            [0,0.9]]

    line = geometry.LineString(polygon_comfortable)
    acceleration = geometry.Point(xG, yG)
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



    ## Jerk tresholds
    #Comfortable
    polygon_comfortable_j = [[-0.6,0], 
                             [0,-0.6], 
                             [0.6,0], 
                             [0,0.6]]

    line = geometry.LineString(polygon_comfortable_j)
    jerk = geometry.Point(Point_X_j, Point_Y_j)
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

    #print(Tcurrent)
    print("Time=  %f    dt=  %f" % ( Tcurrent, dt))
    print("                    X   =  %f    Y   =  %f    Z =  %f" % ( yG, xG, zG))
    print("                    X_j =  %f    Y_j =  %f" % ( Point_X_j, Point_Y_j ))
    comf = comfortAssess()
   
    yGcurrent= yG
    xGcurrent= xG
    Tprev = Tcurrent
    
    
    #Output data to text file
   
    acc.write(str(xG))
    acc.write(",")
    acc.write(str(yG))
    acc.write("\n")
    acc.flush()
        
    j.write(str(Point_X_j))
    j.write(",")
    j.write(str(Point_Y_j))
    j.write("\n")
    j.flush()
    
    lateral.write(str(Tcurrent))
    lateral.write(",")
    lateral.write(str(xG))
    lateral.write("\n")
    lateral.flush()
    
    longitudinal.write(str(Tcurrent))
    longitudinal.write(",")
    longitudinal.write(str(yG))
    longitudinal.write("\n")
    longitudinal.flush()
    
    time1.write(str(time2))
    time1.write("\n")
    time1.flush()

    
        
    
    
    
    
#     comfort.write(str(Tcurrent))
#     comfort.write("   ")
#     comfort.write(str(yG))
#     comfort.write("\n")
#     comfort.flush()
    

    #slow program down a bit, makes the output more readable
    time.sleep(0.1)
 
