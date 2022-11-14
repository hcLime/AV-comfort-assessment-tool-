import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime
import shapely
import shapely.geometry as geometry
import os.path


fig = plt.figure("Comfort score vs Time")
ax1 = fig.add_subplot(1,1,1)

current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M')
file_name = str(current_datetime)

open_path= '/home/chodowi/BerryIMU/python-BerryIMU-measure-G/Data log'
fileName = os.path.join(open_path, file_name+"_score.txt")

def animate(i):
    graph_data = open(fileName,'r').read()
    lines = graph_data.split('\n')
    bs = []
    cs = []
    for line in lines:
        if len(line) > 1:
            b, c, = line.split(',')
            bs.append(float(b))
            cs.append(float(c))

    ax1.clear()
    ax1.plot(bs, cs, color='mediumblue')
    plt.ylim(0,100)
    plt.xlabel("Time [s]",fontsize=12, fontweight= 'bold')
    plt.ylabel("Comfort Score [0-100]",fontsize=12, fontweight= 'bold')
    plt.title('Comfort Score versus Time',fontsize=12, fontweight= 'bold')
    plt.axhline(y=35, color='black', linestyle='-', linewidth= 0.8)
    plt.axhline(y=60, color='red', linestyle='-', linewidth= 0.8)
    plt.axhline(y=65, color='orange', linestyle='-', linewidth= 0.8)
    plt.axhline(y=75, color='gold', linestyle='-', linewidth= 0.8)
    plt.axhline(y=80, color='lime', linestyle='-', linewidth= 0.8)
    plt.axhline(y=90, color='green', linestyle='-', linewidth= 0.8)
    plt.axhline(y=100, color='darkgreen', linestyle='-', linewidth= 0.8)
    plt.grid()

plt.get_current_fig_manager().window.wm_geometry("+1300+50")
ani = animation.FuncAnimation(fig, animate, interval=500)
plt.show()