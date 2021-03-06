import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set matplotlib rc params
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 10}
sns.set(rc=rc)

# load the data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

# make boundaries for bins
low_min = np.min(xa_low)
low_max = np.max(xa_low)
high_max = np.max(xa_high)
high_min = np.min(xa_high)
global_min = np.min((low_min, high_min))
global_max = np.max((low_max, high_max))
bins = np.arange(global_min-50, global_max+50, 50)

# Generate the histogram for the low-density fed mother
_ = plt.hist(xa_low, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
_ = plt.hist(xa_high, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
plt.xlabel('Cross-sectional area (µm$^2$)')
plt.ylabel('count')
plt.legend(('low', 'high'), loc='upper right')
plt.show()

# Save the figure
plt.savefig('egg_area_histograms.svg', bbox_inches='tight')
