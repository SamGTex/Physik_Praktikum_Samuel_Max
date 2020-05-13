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


theta_z , N_z = np.genfromtxt('data/Zink.dat', delimiter=',', unpack=True)
theta_g , N_g = np.genfromtxt('data/Gallium.dat', delimiter=',', unpack=True)
theta_b , N_b = np.genfromtxt('data/Brom.dat', delimiter=',', unpack=True)
theta_r , N_r = np.genfromtxt('data/Rubidium.dat', delimiter=',', unpack=True)
theta_s , N_s = np.genfromtxt('data/Strontium.dat', delimiter=',', unpack=True)
theta_zi , N_zi = np.genfromtxt('data/Zirkonium.dat', delimiter=',', unpack=True)






plt.xlabel(r'$\theta \,/\, \degree$')
plt.ylabel(r'$N \,/\, \frac{Imp}{s}$')
plt.plot(theta_z,N_z,'.',label='Zink')
plt.plot(theta_g,N_g,'.',label='Gallium')
plt.plot(theta_b,N_b,'.',label='Brom')
plt.plot(theta_r,N_r,'.',label='Rubidium')
plt.plot(theta_s,N_s,'.',label='Strontium')
plt.plot(theta_zi,N_zi,'.',label='Zirkonium')
plt.legend(loc='best',)
plt.savefig('absorption1.pdf')
plt.show()