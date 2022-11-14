import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime
import shapely
import shapely.geometry as geometry
import os.path

fig = plt.figure("Longitudinal Acceleration versus Time")
ax1 = fig.add_subplot(1,1,1)

current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M')
file_name = str(current_datetime)

open_path= '/home/chodowi/BerryIMU/python-BerryIMU-measure-G/Data log'
fileName = os.path.join(open_path, file_name+"_longitudinal.txt")

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
    ax1.plot(xs, ys)
    plt.ylim(-6, 6)
    plt.xlabel("Time [s]",fontsize=12, fontweight= 'bold')
    plt.ylabel("Longitudinal Acceleration [m/s2]",fontsize=12, fontweight= 'bold')
    plt.title('Longitudinal Acceleration versus Time',fontsize=12, fontweight= 'bold')
    plt.grid()
    
plt.get_current_fig_manager().window.wm_geometry("+660+550")
ani = animation.FuncAnimation(fig, animate, interval=500)
plt.show()
