import numpy as np
import scipy.stats

# This is how we import the module of Matplotlib
import matplotlib.pyplot as plt

import seaborn as sns
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 10}
sns.set(rc=rc)

# data_txt = np.loadtxt('data/collins_switch.csv', delimiter=',', skiprows=2)

# # Slice out iptg and gfp
# iptg = data_txt[:,0]
# gfp = data_txt[:,1]
# sem = data_txt[:,2]

# # Plot iptg vs. gfp
# plt.semilogx(iptg, gfp, linestyle='none', marker='.', markersize=20)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG titration - semilog X')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.show()

# # Plot iptg vs. gfp
# plt.errorbar(iptg, gfp, yerr=sem, linestyle='none', marker='.',
#                 markersize=20)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG titration - semilog X with errorbars')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.xscale('log')
# plt.show()

def ecdf(data):
    """
    Compute x, y values for an empirial dist. function
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y

# Load egg size data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

x_high, y_high = ecdf(xa_high)
x_low, y_low = ecdf(xa_low)

plt.plot(x_high, y_high, marker='.', linestyle='none', markersize=20)
plt.plot(x_low, y_low, marker='.', linestyle='none', markersize=20)
plt.xlabel('Cross-sectional area (µm)')
plt.ylabel('eCDF')
plt.legend(('high food', 'low food'), loc=('lower right'))
plt.show()
