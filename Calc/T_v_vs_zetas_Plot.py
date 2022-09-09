import matplotlib.pyplot as plt
import numpy as np

I = 30
KV = 190
U = 36
m = 100
incline = 5
r = 0.04

T = 8.27 * I / KV
Th = m * 9.81 * np.sin(np.arctan(5/100)) * r
rpm = KV * U

zetas = np.arange(1,3,.1)

mfontsize = 14
plotsize = .5
fig, TTh = plt.subplots(nrows=1, ncols=1, figsize=(plotsize * 16, plotsize * 9))
TTh.plot(zetas, ((T*zetas)/Th), color="black", ls=":", label="$\\frac{T}{T_{Hang}}$")
vmax = TTh.twinx()
vmax.plot(zetas, ((rpm/zetas)*np.pi*2*r*(60/1000)), color="black", ls="--", label="$v_{max}$")
TTh.set_xlabel("$\\zeta$ / 1", fontsize=mfontsize-2)
TTh.set_ylabel("$\\frac{T}{T_{Hang}}$ / $N \\cdot m$", fontsize=mfontsize-2)
vmax.set_ylabel("$v_{max}$ / $km \\cdot h^{-1}$", fontsize=mfontsize-2)
TTh.set_title("Drehmomentenquotient und Maximalgeschwindigkeit\ngegen $\\zeta$", fontsize=mfontsize+2)
TTh.grid()

vmax.set_ylim(30,100)
TTh.set_ylim(0.6,2.0)

lines, labels = TTh.get_legend_handles_labels()
lines2, labels2 = vmax.get_legend_handles_labels()
vmax.legend(lines + lines2, labels + labels2, loc=7, fontsize=mfontsize-4)

plt.tight_layout()
plt.savefig("Calc\\T_v_vs_zetas.svg", transparent=True)
# plt.show()