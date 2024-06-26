from pylab import *
from matplotlib import animation

k = 2*pi
w = 2*pi
dt = 0.01

xmin = 0
xmax = 3
nbx = 100

x = linspace(xmin, xmax, nbx)

fig = figure() # initialise la figure
line, = plot([],[]) 
xlim(xmin, xmax)
ylim(-1,1)

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line.set_data([],[])
    return line,

def animate(i): 
    t = i * dt
    y = cos(k*x - w*t)
    line.set_data(x, y)
    return line,
 
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, blit=True, interval=20, repeat=False)

show()