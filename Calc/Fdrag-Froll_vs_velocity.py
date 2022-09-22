import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

m = 100						# mass, kg
rho = 1.293					# density of medium, kg/m³
g = 9.81					# gravity, m/s²
A = 0.293					# surface area of body, m²
c_drag = 0.872				# coefficient of drag, 1
c_roll = 0.022				# coefficient of rolling resistance, 1
v = np.linspace(0,50,51)	# velocity, km/h

F_drag = .5 * A * rho * c_drag

mfontsize = 14
plotsize = .5
fig, ratio = plt.subplots(nrows=1, ncols=1, figsize=(plotsize * 18, plotsize * 9))

F_roll = m * g * c_roll
quot = F_drag / F_roll
ratio.plot(v, (quot * (v/3.6)**2), color="black", linewidth=.5, label="$\\frac{F_{Ström}}{F_{Roll}}$")
ratio.set_xlabel("$v$ / $m \\, s^{-1}$", fontsize=mfontsize-2)
ratio.set_ylabel("$\\frac{F_{Ström}}{F_{Roll}}$ / 1", fontsize=mfontsize-2)
ratio.set_title("Quotient aus Strömungs- und Rollwiderstand gegen Geschwindigkeit", fontsize=mfontsize+2)

ratio.xaxis.set_major_locator(MultipleLocator(5))
ratio.xaxis.set_minor_locator(MultipleLocator(2.5))
ratio.yaxis.set_minor_locator(MultipleLocator(.1))

plt.tight_layout()
plt.savefig("Calc\\Fdrag-Froll_vs_velocity.svg", transparent=True)
# plt.show()