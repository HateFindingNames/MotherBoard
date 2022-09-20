import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Calc\\Motherboard_free-wheeling_esc_data.csv', header=1)
data['TimePassedInMs'] = (data['TimePassedInMs'] - data['TimePassedInMs'].min()) * 1e-3

mfontsize = 14
plotsize = .5
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(plotsize * 16, plotsize * 9))
ax.plot(data['TimePassedInMs'], data['Speed'], color='black', ls='solid', label='$v$')
i = ax.twinx()
i.plot(data['TimePassedInMs'], data['Power']/data['MotorCurrent'], color='black', ls=':', label='$U_{Mot}$')
# i.plot(data['TimePassedInMs'], data['MotorCurrent'], color='black', ls=':', label='$I_{Mot}$')

ax.set_title('Verlauf von Motorstrom und\nFahrtgeschwindigkeit im Leerlauf', fontsize=mfontsize+2)
ax.set_xlabel('$t$ / $s$', fontsize=mfontsize-2)
ax.set_ylabel('$v$ / $km\\,h^{-1}$', fontsize=mfontsize-2)
# i.set_ylabel('$I_{Mot}$ / $\\%$', fontsize=mfontsize-2)
i.set_ylabel('$U_{Mot}$ / $V$', fontsize=mfontsize-2)
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = i.get_legend_handles_labels()
ax.legend(lines + lines2, labels + labels2, fontsize=mfontsize-4)

ax.set_xlim(0, data['TimePassedInMs'].max())
ax.set_ylim(0, 25)
# i.set_ylim(0, 100)
# ax.grid()

plt.tight_layout()
# plt.savefig("Calc\\ESC_plot.svg", transparent=True)
plt.show()