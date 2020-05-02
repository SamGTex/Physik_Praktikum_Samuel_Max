import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy.signal import find_peaks
from scipy.stats import sem
import scipy.constants as cn


theta, N = (np.genfromtxt('data/EmissionCu.txt', delimiter=', ', unpack=True))
d = 201.4 * 10**(-12)
def rad(theta):
    return theta*2*np.pi / 360
print(rad(theta))

def welle(alpha):
    E = cn.c * cn.h /(2 *d * np.sin(alpha))
    return E
    
bbox = dict(boxstyle="round", fc="0.8")
#E = c / lamda * h

print(f'kleiner peak bei theta 20.2 und Energie ', welle(rad(20.2)))
print(f'peak bei theta = 22.5 und Energie ', welle(rad(22.5)))


plt.xlabel(r'$\alpha \, / \, °$')
plt.ylabel(r'$N \, / \, Imp/s$')
plt.grid()
plt.plot(theta, N, 'rx', label='Emissionsspektrum')
plt.annotate('Bremsberg', (11.1, 450), (11.25 , 2000), bbox=bbox,arrowprops=dict(arrowstyle = "->"))
plt.annotate(r'$K _\beta$', (20.1, 1599.0), (18 , 1600), bbox=bbox,arrowprops=dict(arrowstyle = "->"))
plt.annotate(r'$K _\alpha$', (22.6, 5050.0), (24 , 5000), bbox=bbox,arrowprops=dict(arrowstyle = "->"))
plt.legend(loc='best')
plt.savefig('Emission.pdf')
plt.show()

#https://www.chemie-biologie.uni-siegen.de/ac/be/lehre/ws1112/roentgen-pulverdiffraktometrie_(xrpd).pdf