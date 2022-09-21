import pandas as pd
import matplotlib.pyplot as plt

# data = pd.read_csv('Calc\\Motherboard_free-wheeling_esc_data.csv', header=1)
data = pd.read_csv('Calc\\Motherboard_test-drive_esc_data.csv', header=1)
data['TimePassedInMs'] = (data['TimePassedInMs'] - data['TimePassedInMs'].min()) * 1e-3
ylims = [data['Speed'].min()-1, data['Speed'].max()+1]

mfontsize = 14
plotsize = .5
fig, (ax, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(plotsize * 18, plotsize * 18))
ax.plot(data['TimePassedInMs'], data['Speed'], color='black', ls='solid', linewidth=.5, label='$v$')
ax2.plot(data['TimePassedInMs'], data['Speed'], color='black', ls='solid', linewidth=.5, label='$v$')
roi = [700, 900]
i = ax.twinx()
i2 = ax2.twinx()
i.plot(data['TimePassedInMs'], data['MotorCurrent'], color='black', linewidth=.5, ls=':', label='$I_{Mot}$')
i2.plot(data['TimePassedInMs'], data['MotorCurrent'], color='black', linewidth=.5, ls=':', label='$I_{Mot}$')

ax.set_title('Verlauf von Motorstrom und Fahrtgeschwindigkeit im Feld', fontsize=mfontsize+2)

ax.set_xlabel('$t$ / $s$', fontsize=mfontsize-2)
ax.set_ylabel('$v$ / $km\\,h^{-1}$', fontsize=mfontsize-2)
ax2.set_xlabel('$t$ / $s$', fontsize=mfontsize-2)
ax2.set_ylabel('$v$ / $km\\,h^{-1}$', fontsize=mfontsize-2)
i.set_ylabel('$I_{Mot}$ / $A$', fontsize=mfontsize-2)
i2.set_ylabel('$I_{Mot}$ / $A$', fontsize=mfontsize-2)

lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = i.get_legend_handles_labels()
ax.legend(lines + lines2, labels + labels2, fontsize=mfontsize-4)
lines, labels = ax2.get_legend_handles_labels()
lines2, labels2 = i2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, fontsize=mfontsize-4)

ax.set_xlim(0, data['TimePassedInMs'].max())
ax.set_ylim(ylims[0], ylims[1])
ax.fill_between(roi, ylims[0], ylims[1], facecolor='black', alpha=0.1)
ax2.set_xlim(roi[0], roi[1])
ax2.set_ylim(ylims[0], ylims[1])
# ax.set_ylim(0, 25)
# i.set_ylim(0, 100)
# ax.grid()

# # inset axes....
# axins = ax.inset_axes([0, -20, 900, data['Speed'].max()])
# # axins.imshow(Z2, extent=extent, origin="lower")
# # sub region of the original image
# x1, x2, y1, y2 = 750, 900, data['Speed'].min(), data['Speed'].max()
# axins.set_xlim(x1, x2)
# axins.set_ylim(y1, y2)
# axins.set_xticklabels([])
# axins.set_yticklabels([])

# ax.indicate_inset_zoom(axins, edgecolor="black")

plt.tight_layout()
plt.savefig("Calc\\ESC_testdrive_plot.svg", transparent=True)
# plt.show()