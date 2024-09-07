# Script for plotting training curves from log files

import numpy as np
import matplotlib.pyplot as plt
import json                         # Oliver added

# Experiment organization/paths
expdir = '/space/oliver/tracr/tracr/experiments/' + '2024_sep_05_initial_experiments/'
val_acc_path = expdir + 'val_acc'
val_loss_path = expdir + 'val_loss'
main_plot_path = expdir + 'plot_val_acc_and_loss'

# Load data
with open(val_acc_path, "r") as fp:
    val_acc = json.load(fp)
with open(val_loss_path, "r") as fp:
    val_loss = json.load(fp)

# Plot data
fig, (ax1,ax2) = plt.subplots(1,2)
ax1.plot(val_loss)
ax1.set(xlabel='training steps',title='val loss')
ax1.grid(linestyle='--')
ax2.plot(val_acc)
ax2.set(xlabel='training steps',title='val acc')
ax2.grid(linestyle='--')
plt.savefig(main_plot_path)
# plt.show()