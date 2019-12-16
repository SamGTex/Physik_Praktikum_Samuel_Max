import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

f, a , b  =np.genfromtxt('python/data/d.csv', delimiter=',', unpack=True)
phi = a/b * 2*np.pi

plt.xlabel(r'$f \,/\, Hz$')
plt.ylabel(r'$ ln(\varphi) $')
plt.grid()
plt.semilogx(f, phi,'rx', label='Messwerte')
plt.legend()
plt.savefig('plotd.pdf')
plt.show()