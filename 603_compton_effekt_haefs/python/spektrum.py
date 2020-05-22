import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy.signal import find_peaks

theta, N = np.genfromtxt('data/EmissionCu.dat', delimiter=',', unpack=True)

plt.xlabel(r'$\theta \,/\, \degree$')
plt.ylabel(r'$N \,/\, \frac{Imp}{s}$')
plt.plot(theta,N,'.',label='Messwerte')
plt.axvline(20.2,color='red',linestyle='--',label=r'$K_\beta$')
plt.axvline(22.5,color='green',linestyle='--',label=r'$K_\alpha$')
plt.annotate('Bremsberg',(11.1,420),xytext=(15,1000),arrowprops=dict(facecolor='black',shrink=0.05))
plt.legend()
plt.savefig('plot.pdf')
plt.show()

print('Peak1:',20.2,1599.0,'lam =','1.39*10^-10', 'E = h*c/lam = ', '1.4282*10^-15')
print('Peak2:',22.5,5050.0,'lam =','1.54*10^-10', 'E = h*c/lam = ', '1.2887*10^-15')