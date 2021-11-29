import matplotlib.pyplot as plt
import numpy as np

#PRESSURE CALIBRATION
pressure0 = np.loadtxt("C:\\Users\\Askar\\PycharmProjects\\pythonProject\\pa0.txt", dtype=float)
pressure = np.loadtxt("C:\\Users\\Askar\\PycharmProjects\\pythonProject\\pa.txt", dtype=float)

p0 = np.mean(pressure0)
p = np.mean(pressure)

pressure_polyfit = np.polyfit([p0, p], [0, 33.3], 1)
pressure_polyval = np.polyval(pressure_polyfit, [p0, p])
pressure_y0 = np.polyval(pressure_polyfit, 0)
pressure_k = 33.3 / (p - p0)

leg = str((" P = {:.3f}N - {:.3f}".format(pressure_k, abs(pressure_y0))))

#PRESSURE CALIBRATION GRAPH
fig1, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot([p0, p], pressure_polyval, label = leg, lw = 2, c = 'red')
ax.set_xlim(p0, p)
ax.set_ylim(min(pressure_polyval), max(pressure_polyval))
ax.set_xlabel("Отсчёты АЦП")
ax.set_ylabel("Давление, Па")
ax.set_title("График калибровки P(N)", fontsize = 20)
ax.legend()
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig1.savefig("C:\\Users\\Askar\\PycharmProjects\\pythonProject\\graph.png")


#DISTANCE CALIBRATION (roflanFace)

k2 = 5 / 900
dist0 = -400
dist = 500
distance_polyval = (k2, [dist0, dist])

leg2 = str(("S (см) = {:.3f}N".format(5/900)))

fig2, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot([-400, 500], pressure_polyval, label = leg2, lw = 2, c = 'red')
ax.set_xlim(dist0, dist)
ax.set_xlabel("Отсчёты АЦП")
ax.set_ylabel("Расстояние, см")
ax.set_title("График калибровки S(N)", fontsize = 20)
fig2.legend()
ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.minorticks_on()
fig2.savefig("C:\\Users\\Askar\\PycharmProjects\\pythonProject\\graph2.png")
