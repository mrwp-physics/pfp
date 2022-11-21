# Thanks to
# https://scipython.com/book2/chapter-7-matplotlib/examples/animating-a-bouncing-ball/

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Acceleration due to gravity, m.s-2.
g = 9.81
# The maximum x-range of ball's trajectory to plot.
XMAX = 5
# The coefficient of restitution for bounces (-v_up/v_down).
cor = 0.65
# The time step for the animation.
dt = 0.005

# Initial position and velocity vectors.
x0, y0 = 0, 4
vx0, vy0 = 1, 0

def get_pos(t=0):
    """A generator yielding the ball's position at time t."""
    x, y, vy = x0, y0, vy0
    while x < XMAX:
        t += dt
        x += vx0 * dt
        y += vy * dt
        vy -= g * dt
        if y < 0:
            # bounce!
            y = 0
            vy = -vy * cor 
        yield x, y,vy




def init():
    """Initialize the animation figure."""
    #animation for s
    ax[0].set_xlim(0, XMAX)
    ax[0].set_ylim(0, y0)
    ax[0].set_xlabel('$s(x)$ /m')
    ax[0].set_ylabel('$s(y)$ /m')
    line1.set_data(xdata, ydata)
    ball1.set_center((x0, y0))
    height_text.set_text(f'Height: {y0:.1f} m')
    #animation for v
    ax[1].set_xlim(0, XMAX)
    #calculation for y lim
    tempy, vy = y0,vy0
    while tempy>0:
        tempy+=vy*dt
        vy -= g*dt
    ax[1].set_ylim(vy,-vy)
    ax[1].set_xlabel('$s(x)$ /m')
    ax[1].set_ylabel('$v(y)$ /m')
    line2.set_data(xdata,vdata)
    ball2.set_center((x0,vy0))


    return line1, ball1, height_text, line2, ball2

def animate(pos):
    """For each frame, advance the animation to the new position, pos."""
    x, y, v = pos
    xdata.append(x)
    ydata.append(y)
    vdata.append(v)
    line1.set_data(xdata, ydata)
    line2.set_data(xdata,vdata)
    ball1.set_center((x, y))
    ball2.set_center((x,v))
    height_text.set_text(f'Height: {y:.1f} m')
    return line1, ball1, height_text,line2,ball2

# Set up a new Figure, with equal aspect ratio so the ball appears round.
fig, ax = plt.subplots(2,constrained_layout = True)
ax[0].set_aspect('equal')

# These are the objects we need to keep track of.
line1, = ax[0].plot([], [], lw=2,color="red")
ball1 = plt.Circle((x0, y0), 0.08,color="red")
height_text = ax[0].text(XMAX*0.5, y0*0.8, f'Height: {y0:.1f} m')
ax[0].add_patch(ball1)
line2, = ax[1].plot([],[],lw=2,color = "blue")
ball2 = plt.Circle((x0,vy0),0.01,color="blue")
ax[1].add_patch(ball2)
xdata, ydata, vdata = [], [],[]

interval = 1000*dt
ani = animation.FuncAnimation(fig, animate, get_pos, blit=True,
                      interval=interval, repeat=False, init_func=init)
plt.show()
