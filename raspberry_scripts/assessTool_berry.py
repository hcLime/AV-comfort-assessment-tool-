#!/usr/bin/python3
#
#       This program assess the vehicle comfort level based on the acceleration input.
#       Accelerations are collected by the LSM6DSL sensor within BerryGPS-IMU V4 unit.
#       Tool outputs comfort assesssment text files, acceleration and jerk data.

import time
import IMU
import sys
import shapely.geometry as geometry
import matplotlib.pyplot as plt
from datetime import datetime
import os.path
from gps import *
from scipy.signal import lfilter


def save(u):
    
    GPS.write(str(long))
    GPS.write(",")
    GPS.write(str(lat))
    GPS.write(",")
    GPS.write(str(u))
    GPS.write(",")
    GPS.flush()
    
def save2(Tcurrent, score):
    
    scor.write(str(Tcurrent))
    scor.write(",")
    scor.write(str(score))
    scor.write("\n")
    scor.flush()
  

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

    Point_X = xG
    Point_Y = yG
    
    cumulativeAcc= (abs(Point_X)+abs(Point_Y))

    if status1 == True and status_j1 == True:
        print('Extremely comfortable')
        score = (100)
        cumulative = (0.6)
        points = (10)
        calc= (cumulativeAcc/cumulative)
        score= (score-(points*calc))
        print(score)
        save(0)
        save2(Tcurrent, score)

    else:
        if status2 == True and status_j2 == True:
            print('Very comfortable')
            score = (90)
            cumulative = (1.2)
            points = (10)
            calc= (cumulativeAcc/cumulative)
            score= str(score-(points*calc))
            print(score)
            save(1)
            save2(Tcurrent, score)

        else:
            if status3 == True and status_j3 == True:
                print('Comfortable')
                score = (80)
                cumulative = (1.8)
                points = (5)
                calc= (cumulativeAcc/cumulative)
                score= float(score-(points*calc))
                print(score)
                save(2)
                save2(Tcurrent, score)
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
                        save2(Tcurrent, score)
                    else:
                        cumulative = (5)
                        calc= (cumulativeAcc/cumulative)
                        score= (score-(points*calc))
                        print(score)
                        save2(Tcurrent, score)
                    save(3)
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
                            save2(Tcurrent, score)
                        else:
                            cumulative = (5.8)
                            calc= (cumulativeAcc/cumulative)
                            score= (score-(points*calc))
                            print(score)
                            save2(Tcurrent, score)
                        save(4)
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
                                save2(Tcurrent, score)
                            else:
                                cumulative = (8.7)
                                calc= (cumulativeAcc/cumulative)
                                score= (score-(points*calc))
                                print(score)
                                save2(Tcurrent, score)
                            save(5)
                        else:
                            print('Extremely uncomfortable')
                            score = (35)
                            cumulative = (15.2)
                            points = (35)
                            calc= (cumulativeAcc/cumulative)
                            score= (score-(points*calc))
                            print(score)
                            save2(Tcurrent, score)
                            save(6)
    return
 
    
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
completeName5 = os.path.join(save_path, file_name+"_utime.txt") #save utime for every timestep
completeName6 = os.path.join(save_path, file_name+"_GPS.txt") # save long, lot position with comfort score
completeName7 = os.path.join(save_path, file_name+"_jlateral.txt")
completeName8 = os.path.join(save_path, file_name+"_jlongitudinal.txt")
completeName9 = os.path.join(save_path, file_name+"_altitude.txt")
completeName10 = os.path.join(save_path, file_name+"_speed.txt")
completeName11 = os.path.join(save_path, file_name+"_score.txt")


lateral = open(completeName1, 'a')
longitudinal = open(completeName2, 'a')
acc = open(completeName3, 'a')
j = open(completeName4, 'a')
time1 = open(completeName5, 'a')
GPS = open(completeName6, 'a')
jlat = open(completeName7, 'a')
jlong = open(completeName8, 'a')
alt= open(completeName9, 'a')
spd= open(completeName10, 'a')
scor= open(completeName11, 'a')

lat=0
long=0
time3=0
Point_X_j = 0
Point_Y_j = 0

#initialise GPS
#gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)


while True:
    
    #report = gpsd.next()
    #lat= getattr(report,'lat', 0.0)
    #long= getattr(report,'lon', 0.0)
    #speed= getattr(report,'speed','nan')
    #alti= getattr(report,'alt','nan')
    #time3= getattr(report,'time','')
    
    #if report['class'] == 'TPV':
            
            #lat= getattr(report,'lat', 0.0)
            #long= getattr(report,'lon', 0.0)
            #time3= getattr(report,'time','')
            #time.sleep(0.1)
            
            #print(getattr(report,'alt','nan'),"\t\t"),
            #print(getattr(report,'epv','nan'),"\t"),
            #print(getattr(report,'ept','nan'),"\t"),
            #print(getattr(report,'speed','nan'),"\t"),
            #print(getattr(report,'climb','nan'),"\t")
    
    time2 = time.time()   
    Tcurrent = time2-t
    dt = Tcurrent-Tprev #timestep

    #Read the accelerometer,gyroscope and magnetometer values
    ACCx = IMU.readACCx()
    ACCy = IMU.readACCy()
    ACCz = IMU.readACCz()
    #yG = (ACCx * 0.244)/1000
    #xG = (ACCy * 0.244)/1000
    #zG = (ACCz * 0.244)/1000
    
    #xG= []
    #yG= []
    
    # get more accurate G value / read more about accuaracy of IMU sensor
    # Macro for mg per LSB at +/- 2g sensitivity (1 LSB = 0.000244mg)
    # Macro for mg per LSB at +/- 4g sensitivity (1 LSB = 0.000488mg)
    # Macro for mg per LSB at +/- 8g sensitivity (1 LSB = 0.000976mg)
    xG =  9.80665*(ACCx * 0.000244)
    yG =  9.80665*(ACCy * 0.000244)
    zG =  9.80665*(ACCz * 0.000244)- 9.80665
    #print("##### X = %fG  ##### Y =   %fG  ##### Z =  %fG  #####" % ( ACCy, ACCx, ACCz)) #G values
    
    
    #lfilter
    #Xacc.append(float(xG))
    #Yacc.append(float(yG))

    #n=15
    #b=[1.0 / n]
    #a=1
    #filtX = lfilter(b,a,Xacc)
    #filtY = lfilter(b,a,Yacc)
    
    #filXcurrent = filtX[-1]
    #filXprev = filtX[-2]
    #filYcurrent = filtY[-1]
    #filYprev = filtY[-2]
     
    #Point_X_j= (filXcurrent-filXprev)/dt #Lateral jerk
    #Point_Y_j= (filYcurrent-filYprev)/dt #Longitudinal jerk
    
    
    
    #Point_X_j= (xG-xGprev)/dt #Lateral jerk
    #Point_Y_j= (yG-yGprev)/dt #Longitudinal jerk
    
    
    ##  Acceleration tresholds 
    #Extremely comfortable
    polygon_ecomfortable = [[-0.3,0], 
                            [0,-0.3], 
                            [0.3,0], 
                            [0,0.3]]

    line = geometry.LineString(polygon_ecomfortable)
    acceleration = geometry.Point(xG, yG)
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

    point= geometry.Point([xG, yG])


    ## Jerk tresholds
    #Extremely comfortable
    polygon_ecomfortable_j = [[-0.2,0], 
                             [0,-0.2], 
                             [0.2,0], 
                             [0,0.2]]

    line = geometry.LineString(polygon_ecomfortable_j)
    jerk = geometry.Point(Point_X_j, Point_Y_j)
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
    
   

    #print(Tcurrent)
    print("lat=  %f    long=  %f" % (lat, long))
    print("Time=  %f    dt=  %f" % ( Tcurrent, dt))
    print("                    X   =  %f    Y   =  %f    Z =  %f" % ( yG, xG, zG))
    print("                    X_j =  %f    Y_j =  %f" % ( Point_X_j, Point_Y_j ))
    
    
    
    #change current timestep to previous timestep
    yGprev= yG
    xGprev= xG
    Tprev = Tcurrent
    
    comf = comfortAssess() #assess comfort 
    
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
    
    jlat.write(str(Tcurrent))
    jlat.write(",")
    jlat.write(str(Point_X_j))
    jlat.write("\n")
    jlat.flush()
    
    jlong.write(str(Tcurrent))
    jlong.write(",")
    jlong.write(str(Point_Y_j))
    jlong.write("\n")
    jlong.flush()
    
    #alt.write(str(Tcurrent))
    #alt.write(",")
    #alt.write(str(alti))
    #alt.write("\n")
    #alt.flush()
    
    #spd.write(str(Tcurrent))
    #spd.write(",")
    #spd.write(str(speed))
    #spd.write("\n")
    #spd.flush()
    
    


    

    
    
#     comfort.write(str(Tcurrent))
#     comfort.write("   ")
#     comfort.write(str(yG))
#     comfort.write("\n")
#     comfort.flush()
    
    #timestep
    time.sleep(0.1)

 
