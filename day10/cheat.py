import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
import numpy as np
import re

with open('data') as file:
    lines = file.readlines()
    lines = [[int(i) for i in re.findall(r'-?\d+', l)] for l in lines]

data = np.array(lines, dtype=np.float32)
p = data[:, :2]
v = data[:, 2:]

px = p[:, 0]
vx = v[:, 0]

mu = np.mean(px)
ev = np.mean(vx)
t = np.mean((mu - px) / (vx - ev))

t = int(round(t))-1

print(t)


POSx=p[:,0]
POSy=p[:,1]
VELx=v[:, 0]
VELy=v[:, 1]

print(POSx[0:5],POSy[0:5],VELx[0:5],VELy[0:5])
x=POSx
y=POSy
for k in range(len(POSx)):
    x[k] += VELx[k] * t
    y[k] += VELy[k] * t

maxx=max(x)
maxy=max(y)
minx=min(x)
miny=min(y)

fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0, 0, 1, 1], frameon=True)
ax.set_xlim(minx, maxx), ax.set_xticks([])
ax.set_ylim(minx, maxx), ax.set_yticks([])

points=ax.plot(x,y,'.')
plt.show()

print(t)