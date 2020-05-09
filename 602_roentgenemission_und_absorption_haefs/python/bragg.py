import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

theta, N = np.genfromtxt('data/Bragg.dat', delimiter=',', unpack=True)
peak = find_peaks(N,150)
d = 201.4*10**(-12) #m
print('Peak:')
print('(theta , N) =', '(', 28.2,',',218,')')
print('lam_max_E =',2*d*np.sin(np.radians(28.2)))
plt.xlabel(r'$\lambda \,/\, m$')
plt.ylabel(r'$N \,/\, \frac{Imp}{s}$')
plt.plot(2*d*np.sin(np.radians(theta)), N, 'b.')
plt.grid()
plt.savefig('build/bragg.pdf')
plt.show()