import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime
import shapely
import shapely.geometry as geometry
import os.path

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

x1, y1 = polygon_comfortable_j.exterior.xy
x2, y2 = polygon_normal_j.exterior.xy
x3, y3 = polygon_aggresive_j.exterior.xy

fig = plt.figure("Jerk")
plt.grid()
ax1 = fig.add_subplot(1,1,1)

current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M')
file_name = str(current_datetime)

open_path= '/home/chodowi/BerryIMU/python-BerryIMU-measure-G/Data log'
fileName = os.path.join(open_path, file_name+"_jerk.txt")

def animate(i):
    graph_data = open(fileName,'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
            
    ax1.clear()
    ax1.plot(xs, ys, '.', color="black")
    plt.plot(x1, y1, color="green") 
    plt.plot(x2, y2, color="orange")
    plt.plot(x3, y3, color="red")
    plt.xlim(-2.2, 2.2)
    plt.ylim(-2.2, 2.2)
    plt.xlabel("Lateral Acceleration [m/s2]")
    plt.ylabel("Longitudinal Acceleration [m/s2]")
    plt.grid()
    

ani = animation.FuncAnimation(fig, animate, interval=500)
plt.show()
