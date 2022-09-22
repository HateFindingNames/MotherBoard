import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# data = pd.read_csv('Calc\\Motherboard_free-wheeling_esc_data.csv', header=1)
data = pd.read_csv('Calc\\Motherboard_test-drive_esc_data.csv', header=1)
data['TimePassedInMs'] = (data['TimePassedInMs'] - data['TimePassedInMs'].min()) * 1e-3
ylims = [data['Speed'].min()-1, data['Speed'].max()+1]
data['Distance'] = (data['Distance'] - data['Distance'].min()) * 1000
distAtMax = data.loc[data['Speed'] == data['Speed'].max(), 'Distance'].values[0]

mfontsize = 14
plotsize = .5
fig, (ax, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(plotsize * 18, plotsize * 9), gridspec_kw={'height_ratios': [1.25, 2]})

ax.plot(data['Distance'], data['Speed'], color='black', ls='solid', linewidth=.5, label='$v$')
ax2.plot(data['Distance'], data['Speed'], color='black', ls='solid', linewidth=.5, label='$v$')
i = ax.twinx()
i2 = ax2.twinx()
i.plot(data['Distance'], data['MotorCurrent'], color='black', linewidth=.5, ls=':', label='$I_{Mot}$')
i2.plot(data['Distance'], data['MotorCurrent'], color='black', linewidth=.5, ls=':', label='$I_{Mot}$')

ax.set_title('Verlauf von Motorstrom und Fahrtgeschwindigkeit\nentlang einer Teststrecke im Feld', fontsize=mfontsize+2)

ax.set_xlabel('$s$ / $m$', fontsize=mfontsize-2)
ax.set_ylabel('$v$ / $km\\,h^{-1}$', fontsize=mfontsize-2)
ax2.set_xlabel('$s$ / $m$', fontsize=mfontsize-2)
ax2.set_ylabel('$v$ / $km\\,h^{-1}$', fontsize=mfontsize-2)
i.set_ylabel('$I_{Mot}$ / $A$', fontsize=mfontsize-2)
i2.set_ylabel('$I_{Mot}$ / $A$', fontsize=mfontsize-2)

lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = i.get_legend_handles_labels()
ax.legend(lines + lines2, labels + labels2, fontsize=mfontsize-4)
lines, labels = ax2.get_legend_handles_labels()
lines2, labels2 = i2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, fontsize=mfontsize-4)

roi = [1300, 1800]
ax.fill_between(roi, ylims[0], ylims[1], facecolor='black', alpha=0.1)

ax.set_ylim(ylims[0], ylims[1])
ax2.set_xlim(roi[0], roi[1])
ax2.set_ylim(ylims[0], ylims[1])

ax.xaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_minor_locator(MultipleLocator(250))
ax.yaxis.set_minor_locator(MultipleLocator(2.5))
i.yaxis.set_minor_locator(MultipleLocator(5))
ax2.xaxis.set_minor_locator(MultipleLocator(50))
ax2.yaxis.set_minor_locator(MultipleLocator(2.5))
i2.yaxis.set_minor_locator(MultipleLocator(5))

# ax2.arrow(distAtMax-2, data['Speed'].max()-1, -50, -15)
# ax2.annotate(str(round(data['Speed'].max(), 1)), [distAtMax, data['Speed'].max()], [-50, -15])
ax2.annotate(str(round(data['Speed'].max(), 1)), xy=(distAtMax, data['Speed'].max()), xycoords='data', xytext=(1700, 6), textcoords='data',
	arrowprops=dict(arrowstyle="->", connectionstyle="arc3", linewidth=.8))

plt.tight_layout()
plt.savefig("Calc\\ESC_testdrive_plot.svg", transparent=True)
# plt.show()