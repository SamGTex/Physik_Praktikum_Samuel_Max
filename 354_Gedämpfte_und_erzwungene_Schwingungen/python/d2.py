import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

f,a,b=np.genfromtxt('python/data/d.csv', delimiter=',', unpack=True)
phi = a/b * 2*np.pi

print(phi)
plt.xlabel(r'$f \,/\, Hz$')
plt.ylabel(r'$ \varphi $')
plt.grid()
plt.plot(f, phi,'rx', label='Messwerte')
plt.legend()
plt.savefig('plotd2.pdf')
plt.show()
