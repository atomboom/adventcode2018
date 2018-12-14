import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time






filename='data'
file=open(filename,mode='r')
data = file.read().splitlines()

data=list(map(str,data)) #data to string. list

POSx=[0]
POSy=[0]
VELx=[0]
VELy=[0]
for i in range(len(data)):
    sw=data[i].index('vel')
    pos=data[i][0:sw]
    vel = data[i][sw:]

    POSx.append(int(pos[pos.index('=<')+2:pos.index(',')]))
    POSy.append(int(pos[pos.index(',')+1:pos.index('>')]))
    VELx.append(int(vel[pos.index('=<')+2:vel.index(',')]))
    VELy.append(int(vel[vel.index(',')+1:vel.index('>')]))






minx=min(POSx)
miny=min(POSy)

for i in range(len(data)):
    POSx[i] +=abs(minx)
    POSy[i] += abs(miny)

minx=min(POSx)
miny=min(POSy)
maxx=max(POSx)
maxy=max(POSy)

maxax=max([maxx,maxy])



# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0, 0, 1, 1], frameon=True)
ax.set_xlim(0, maxax), ax.set_xticks([])
ax.set_ylim(0, maxax), ax.set_yticks([])


x=POSx
y=POSy







d=1
score=[]
min_score=[10**7,0]

for i in range(0,10000):

    for k in range(len(x)):
        x[k] += VELx[k] * d
        y[k] += VELy[k] * d

    avgx= sum(x)/len(x)
    avgy = sum(y) / len(y)
    temp=0

    if avgx>0 and avgy>0:
        for k in range(len(x)):
            temp=+abs(x[k]-avgx)+abs(y[k]-avgy)

        if temp <min_score[0]:
            min_score=[temp,i]
            # print('jipie kay yah:',min_score,avgx,avgy,min_score[1]*d)


singul_step=d*(min_score[1]-220)
print(singul_step)

x=POSx
y=POSy

print(x[1])
for k in range(len(x)):
    x[k] += (VELx[k] * singul_step)
    y[k] += (VELy[k] * singul_step)
print(x[1])


points = ax.plot(x,y,'.')

avgx= sum(x)/len(x)
avgy = sum(y) / len(y)



ax_min=50300
ax_max=50500
d=100
def update(frame_number):
    # Get an index which we can use to re-spawn the oldest raindrop.
    current_index = frame_number

    if x[100]>ax_min and x[100]<ax_max:
        d=-1
        print('slowdonw',frame_number)
        input("Press Enter to continue...")
    else:
        d=-80
    for i in range(len(x)):
        x[i]+= VELx[i]*d
        y[i]+= VELy[i]*d

    maxax=max(max(x),max(y))
    minax = min(min(x), min(y))
    ax.clear()
    ax.set_xlim(ax_min, ax_max), ax.set_xticks([])
    ax.set_ylim(ax_min, ax_max), ax.set_yticks([])
    points=ax.plot(x,y,'.')
    print(x[100],frame_number)




# Construct the animation, using the update function as the animation
# director.
animation = FuncAnimation(fig, update, interval=5)
plt.show()