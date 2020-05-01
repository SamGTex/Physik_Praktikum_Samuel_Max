import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy.signal import find_peaks
from scipy.stats import sem

theta, N = (np.genfromtxt('data/EmissionCu.txt', delimiter=', ', unpack=True))


plt.xlabel(r'$theta \, / \, °$')
plt.ylabel(r'$N \, / \, Imp/s$')
plt.grid()
plt.plot(theta, N, 'g-', label='Emissionsspektrum')
plt.legend(loc='best')
plt.savefig('Emission.pdf')
plt.show
print(f'kleiner peak bei theta 20.2 und N = 1599.0')
print(f'peak bei theta = 22.5 und N = 5050.0')
