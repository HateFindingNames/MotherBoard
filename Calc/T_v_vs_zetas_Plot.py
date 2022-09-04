import matplotlib.pyplot as plt
import numpy as np

T = 1.306
Th = 1.96
rpm = 190 * 36

zetas = np.arange(1,3,.1)

mfontsize = 14
plotsize = .5
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(plotsize * 16, plotsize * 9))
ax.plot(zetas, ((T*zetas)/Th), color="black", ls=":", label="$\\frac{T}{T_{Hang}}$")
ax2 = ax.twinx()
ax2.plot(zetas, ((rpm/zetas)*np.pi*0.08*(60/1000)), color="black", ls="--", label="$v_{max}$")
ax.grid()


ax.set_title("Drehmomentenquotient und Maximalgeschwindigkeit gegen $\\zeta$", fontsize=mfontsize)
ax.set_xlabel("$\\zeta$ / 1", fontsize=mfontsize-2)
ax.set_ylabel("$\\frac{T}{T_{Hang}}$ / $N \\cdot m$", fontsize=mfontsize-2)
ax2.set_ylabel("$v$ / $km \\cdot h^{-1}$", fontsize=mfontsize-2)

ax2.set_ylim(30,100)
ax.set_ylim(0.6,2.0)

lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=7, fontsize=mfontsize-4)
# ax.legend()
# ax2.legend()

plt.tight_layout()
plt.savefig("Calc\\T_v_vs_zetas.svg", transparent=True)
plt.show()