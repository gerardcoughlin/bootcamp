import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

# The x-values we want
x = np.linspace(-15, 15, 400)

# The normalized intensity
norm_I = 4 * (scipy.special.j1(x) / x)**2

# plot our computation
plt.plot(x, norm_I)
plt.xlabel('$x$')
plt.ylabel('$I(x)/I_0$')

# Processing the spike data.
data = np.loadtxt('data/retina_spikes.csv', skiprows=2, delimiter=',')
t = data[:,0]
V = data[:,1]

# Close all other plots, just in case
plt.close()
plt.plot(t, V)
plt.xlabel('t (ms)')
plt.ylabel('V (µV)')
plt.show()
