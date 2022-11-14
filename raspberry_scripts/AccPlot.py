import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime
import shapely
import shapely.geometry as geometry
import os.path

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

#Plotting tresholds
x1, y1 = polygon_ecomfortable.exterior.xy
x2, y2 = polygon_vcomfortable.exterior.xy
x3, y3 = polygon_comfortable.exterior.xy
x4, y4 = polygon_acceptable.exterior.xy
x5, y5 = polygon_poor.exterior.xy
x6, y6 = polygon_uncomfortable.exterior.xy


fig = plt.figure("Longitudinal/Lateral Acceleration Classification")
plt.grid()
ax1 = fig.add_subplot(1,1,1)

current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M')
file_name = str(current_datetime)

open_path= '/home/chodowi/BerryIMU/python-BerryIMU-measure-G/Data log'
fileName = os.path.join(open_path, file_name+"_acc.txt")

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
    plt.plot(x1, y1, color="darkgreen", label='A*', linewidth= 1.8)
    plt.plot(x2, y2, color="green", label='A', linewidth= 1.8)
    plt.plot(x3, y3, color="lime", label='B', linewidth= 1.8)
    plt.plot(x4, y4, color="gold", label='C', linewidth= 1.8)
    plt.plot(x5, y5, color="orange", label='D', linewidth= 1.8)
    plt.plot(x6, y6, color="red", label='E', linewidth= 1.8)
    plt.xlabel("Lateral Acceleration [m/s2]",fontsize=12, fontweight= 'bold')
    plt.ylabel("Longitudinal Acceleration [m/s2]", fontsize=12, fontweight= 'bold')
    plt.title('Longitudinal/Lateral Acceleration Classification',fontsize=12, fontweight= 'bold')
    plt.legend(loc='lower right')
    plt.grid()


plt.get_current_fig_manager().window.wm_geometry("+660+50")

ani = animation.FuncAnimation(fig, animate, interval=500)
plt.show()



