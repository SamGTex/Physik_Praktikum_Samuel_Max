import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy.signal import find_peaks
from scipy.stats import sem
import scipy.constants as cn
from uncertainties import ufloat
#from uncertainties import uarray
from uncertainties import unumpy as unp

theta , N = np.genfromtxt('data/Bragg.dat', delimiter=',', unpack=True)

print('Maximum bei :', 28.2,  218.0)

plt.xlabel(r'$\theta \,/\, \degree$')
plt.ylabel(r'$N \,/\, \frac{Imp}{s}$')
plt.plot(theta,N,'.',label='Emissionsspektrum')
plt.legend(loc='best',)
plt.savefig('absorption1.pdf')
plt.show()