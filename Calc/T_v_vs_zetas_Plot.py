import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

I = 30						# Motor current, A
KV = 190					# Motor Speed constant, 1/(min*V)
U = 36						# battery voltage, V
incline = 5					# slope incline, %
r = 0.04					# wheel dia, m
m = 100						# mass, kg
rho = 1.204					# density of medium, kg/m³
g = 9.81					# gravity, m/s²
A = 0.293					# surface area of body, m²
c_drag = 0.872				# coefficient of drag, 1
c_roll = 0.022				# coefficient of rolling resistance, 1
v = 10						# velocity, km/h

F_incl = m * g * (np.sin(np.arctan(5/100)))
F_drag = .5 * A * rho * c_drag * (v/3.6)**2
F_roll = m * g * c_roll

T = 8.27 * I / KV
Th = (F_incl + F_drag + F_roll) * r
rpm = KV * U

zetas = np.arange(1,3,.1)

mfontsize = 14
plotsize = .5
fig, TTh = plt.subplots(nrows=1, ncols=1, figsize=(plotsize * 18, plotsize * 9))
TTh.plot(zetas, ((T*zetas)/Th), color="black", ls="solid", linewidth=.5, label="$\\frac{T}{T_{Hang}}$")
vmax = TTh.twinx()
vmax.plot(zetas, ((rpm/zetas)*np.pi*2*r*(60/1000)), color="black", ls="--", linewidth=.5, label="$v_{max}$")
TTh.set_xlabel("$\\zeta$ / 1", fontsize=mfontsize-2)
TTh.set_ylabel("$\\frac{T}{T_{Hang}}$ / $N \\, m$", fontsize=mfontsize-2)
vmax.set_ylabel("$v_{max}$ / $km \\, h^{-1}$", fontsize=mfontsize-2)
TTh.set_title("Drehmomentenquotient und Maximalgeschwindigkeit gegen $\\zeta$", fontsize=mfontsize+2)

TTh.xaxis.set_minor_locator(MultipleLocator(.125))
TTh.yaxis.set_minor_locator(MultipleLocator(.1))
vmax.yaxis.set_minor_locator(MultipleLocator(5))

lines, labels = TTh.get_legend_handles_labels()
lines2, labels2 = vmax.get_legend_handles_labels()
vmax.legend(lines + lines2, labels + labels2, loc=7, fontsize=mfontsize-4)

plt.tight_layout()
plt.savefig("Calc\\T_v_vs_zetas.svg", transparent=True)
# plt.show()