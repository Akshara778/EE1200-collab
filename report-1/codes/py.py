import math
import matplotlib.pyplot as plt
import numpy as np

def ramp(frequency, amplitude, num_points, start_phase=0):
    t = np.linspace(0, 1, num_points)
    wave = []
    for i in t:
        wave.append((2.0 * amplitude / math.pi) * math.acos(math.cos(((2 * math.pi * frequency) * i) + start_phase)) - amplitude)
    return wave
    
def sin(amplitude, frequency, num_points, phase_shift=0):
    t = np.linspace(0, 1, num_points)
    wave = amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
    return wave


#Figure-1
plt.figure()
coord_sin1 = sin(13, 1, 7000, 0)
coord_sin2 = sin(4, 5, 7000, math.pi*0.5)
plt.plot(coord_sin1, coord_sin2)
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-20,20)
plt.ylim(-10,10)
plt.grid(True)
ax = plt.gca()
ax.xaxis.set_tick_params(labelbottom=False)
ax.yaxis.set_tick_params(labelleft=False)
plt.savefig("../figs/fig1.png")

#Figure-2
plt.figure()
coord_sin1 = sin(7, 2, 7000, 0)
coord_sin2 = sin(7, 1, 7000, 0)
plt.plot(coord_sin1, coord_sin2)
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-20,20)
plt.ylim(-10,10)
plt.grid(True)
ax = plt.gca()
ax.xaxis.set_tick_params(labelbottom=False)
ax.yaxis.set_tick_params(labelleft=False)
plt.savefig("../figs/fig2.png")

#Figure-3
plt.figure()
coord_sin1 = sin(7, 1, 7000, 0)
coord_sin2 = sin(7, 1, 7000, math.radians(150))
plt.plot(coord_sin1, coord_sin2)
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-20,20)
plt.ylim(-10,10)
plt.grid(True)
ax = plt.gca()
ax.xaxis.set_tick_params(labelbottom=False)
ax.yaxis.set_tick_params(labelleft=False)
plt.savefig("../figs/fig3.png")

#Figure-4
plt.figure()
coord_ramp1 = ramp(3, 13, 7000, 0)
coord_ramp2 = ramp(16, 5, 7000, math.pi)
plt.plot(coord_ramp1, coord_ramp2)
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-20,20)
plt.ylim(-15,15)
plt.grid(True)
ax = plt.gca()
ax.xaxis.set_tick_params(labelbottom=False)
ax.yaxis.set_tick_params(labelleft=False)
plt.savefig("../figs/fig4.png")

#Figure-5
plt.figure()
coord_ramp1 = ramp(3, 13, 7000, 0)
coord_ramp2 = ramp(16, 5, 7000, math.radians(180 + (35 * 180/65.0)))
plt.plot(coord_ramp1, coord_ramp2)
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-20,20)
plt.ylim(-12,12)
plt.grid(True)
ax = plt.gca()
ax.xaxis.set_tick_params(labelbottom=False)
ax.yaxis.set_tick_params(labelleft=False)
plt.savefig("../figs/fig5.png")

#Figure-6
plt.figure()
coord_sin = sin(13, 1, 7000, 0)
coord_ramp = ramp(2, 4, 7000, math.radians(45))
plt.plot(coord_sin, coord_ramp)
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-20,20)
plt.ylim(-10,10)
plt.grid(True)
ax = plt.gca()
ax.xaxis.set_tick_params(labelbottom=False)
ax.yaxis.set_tick_params(labelleft=False)
plt.savefig("../figs/fig6.png")

#Figure-7
plt.figure()
coord_sin1 = sin(13, 1, 7000, 0)
coord_sin2 = sin(4, 12, 7000, math.radians(-90))
plt.plot(coord_sin1, coord_sin2)
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-20,20)
plt.ylim(-10,10)
plt.grid(True)
ax = plt.gca()
ax.xaxis.set_tick_params(labelbottom=False)
ax.yaxis.set_tick_params(labelleft=False)
plt.savefig("../figs/fig7.png")
