import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

# generate bootstrap replicates for 1975
n_reps = 100000
bs_replicates_1975 = np.empty(n_reps)
for i in range(n_reps):
    bs_sample = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
    bs_replicates_1975[i] = np.mean(bs_sample)

conf_int_1975 = np.percentile(bs_replicates_1975, [2.5, 97.5])

def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

# generate bootstrap replicates for 2012
n_reps = 100000
bs_replicates_2012 = np.empty(n_reps)
for i in range(n_reps):
    bs_sample = np.random.choice(bd_2012, replace=True, size=len(bd_2012))
    bs_replicates_2012[i] = np.mean(bs_sample)

conf_int_2012 = np.percentile(bs_replicates_2012, [2.5, 97.5])

def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

# # Compute ECDFs for 1975 and 2012
# x_1975, y_1975 = ecdf(bd_1975)
# x_2012, y_2012 = ecdf(bd_2012)
# x_1975_bs, y_1975_bs = ecdf(bs_sample)

# # Plot the ECDFs
# plt.plot(x_1975, y_1975, marker='.', linestyle='none')
# plt.plot(x_2012, y_2012, marker='.', linestyle='none')
# plt.margins(0.02)
# plt.xlabel('beak depth (mm)')
# plt.ylabel('ECDF')
# plt.legend(('1975', '2012'), loc='lower right')
# plt.show()

# # Plot the ECDFs
# plt.plot(x_1975, y_1975, marker='.', linestyle='none')
# plt.plot(x_1975_bs, y_1975_bs, marker='.', linestyle='none')
# plt.margins(0.02)
# plt.xlabel('beak depth (mm)')
# plt.ylabel('ECDF')
# plt.legend(('1975', 'bootstrap'), loc='lower right')
# plt.show()
