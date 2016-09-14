import numpy as np
import scipy.stats

# This is how we import the module of Matplotlib
import matplotlib.pyplot as plt

import seaborn as sns
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 10}
sns.set(rc=rc)

# load data sets
wt_data = np.loadtxt('data/wt_lac.csv', delimiter=',', skiprows=3)
m_data = np.loadtxt('data/q18m_lac.csv', delimiter=',', skiprows=3)
a_data = np.loadtxt('data/q18a_lac.csv', delimiter=',', skiprows=3)

# slice out data
wt_iptg = wt_data[:,0]
wt_fold = wt_data[:,1]
m_iptg = m_data[:,0]
m_fold = m_data[:,1]
a_iptg = a_data[:,0]
a_fold = a_data[:,1]

# # plot iptg vs. fold
# plt.semilogx(wt_iptg, wt_fold, linestyle='none', marker='.', markersize=20)
# plt.semilogx(m_iptg, m_fold, linestyle='none', marker='.', markersize=20)
# plt.semilogx(a_iptg, a_fold, linestyle='none', marker='.', markersize=20)
# plt.legend(('WT', 'q18m', 'q18a'), loc=('lower right'))
# plt.xlabel('[IPTG] (mM)')
# plt.ylabel('Fold difference')
# plt.show()

# calculate theoretical fold change
def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """Calculate the theoretical fold change in expression"""
    upper = RK * (1 + (c / KdA) ** 2)
    lower_l = (1 + (c / KdA) ** 2)
    lower_r = Kswitch * ((1 + (c / KdI) ** 2))
    fold_c = 1 / (1 + upper / (lower_l + lower_r))
    return fold_c

# important numbers
theo_c = np.logspace(-6, 2)
wt_RK = 141.4
a_RK = 16.56
m_RK = 1332

# theoretical fold changes
wt_theo_fold = fold_change(theo_c, wt_RK)
a_theo_fold = fold_change(theo_c, a_RK)
m_theo_fold = fold_change(theo_c, m_RK)

# # plot iptg vs. fold with theoretical
# colors = sns.color_palette()
# plt.semilogx(wt_iptg, wt_fold, linestyle='none', marker='.', markersize=20)
# plt.semilogx(theo_c, wt_theo_fold, color=colors[0])
# plt.semilogx(m_iptg, m_fold, linestyle='none', marker='.', markersize=20)
# plt.semilogx(theo_c, m_theo_fold, color=colors[1])
# plt.semilogx(a_iptg, a_fold, linestyle='none', marker='.', markersize=20)
# plt.semilogx(theo_c, a_theo_fold, color=colors[2])
# plt.legend(('WT', 'q18m', 'q18a'), loc=('lower right'))
# plt.xlabel('[IPTG] (mM)')
# plt.ylabel('Fold difference')
# plt.show()

# calculate Bohr parameter
def bohr_parameter(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """Calculate the Bohr parameter"""
    bohr_param = (1 + c/KdA)**2 / ((1 + c/KdA)**2 + Kswitch*(1 + c/KdI)**2)
    return -np.log(RK) - np.log(bohr_param)

# calculate the fold change from Bohr parameter
def fold_change_bohr(bohr_parameter):
    """Calculate the fold change from the Bohr parameter"""
    return 1 / (1 + np.exp(-bohr_parameter))

# generate values for Bohr parameter
theo_bohr = np.linspace(-6, 6, 200)
theo_bohr_fc = fold_change_bohr(theo_bohr)

# convert actual concentrations to Bohr parameter and plot
wt_bohr = bohr_parameter(wt_data[:,0], wt_RK)
plt.plot(wt_bohr, wt_data[:,1], marker='.', linestyle='none')
a_bohr = bohr_parameter(a_data[:,0], a_RK)
plt.plot(a_bohr, a_data[:,1], marker='.', linestyle='none')
m_bohr = bohr_parameter(m_data[:,0], m_RK)
plt.plot(m_bohr, m_data[:,1], marker='.', linestyle='none')
plt.plot(theo_bohr, theo_bohr_fc, color='gray')
plt.xlabel('Bohr parameter')
plt.ylabel('fold change')
plt.legend(('wt', 'q18a', 'q18m', 'theoretical'), loc='lower right')
