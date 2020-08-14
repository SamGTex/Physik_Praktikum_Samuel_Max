import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
#from scipy.interpolate import interp1d
#from scipy.signal import find_peaks
from scipy import stats
from scipy.stats import sem
import scipy.constants as cn
from uncertainties import ufloat
#from uncertainties import unumpy as unp

g, b, B = (np.genfromtxt('data/abbe.csv', delimiter=', ', unpack=True))

G = 3

V = B/G

## Ausgleichsgeraden
def f(x,a,b):
    return a*x + b

# für g
params_g,pcov_g = curve_fit(f,(1+1/V),g)
a_g = ufloat(params_g[0],np.absolute(pcov_g[0][0])**0.5)
b_g = ufloat(params_g[1],np.absolute(pcov_g[1][1])**0.5)

# für b
params_b,pcov_b = curve_fit(f,(1+V),b)
a_b = ufloat(params_b[0],np.absolute(pcov_b[0][0])**0.5)
b_b = ufloat(params_b[1],np.absolute(pcov_b[1][1])**0.5)

# Abstand der Hauptebenen
d = b_b - b_g


## Plot g'
print("Plot nach Abbe für g")

# Plot der Ausgleichsgerade
g_linspace = np.linspace(np.min(1+1/V),np.max(1+1/V),100)
plt.plot(g_linspace, f(g_linspace,*params_g), 'k-', label="Ausgleichsgerade")

# Plot der Daten
plt.plot((1+1/V), g, 'ro', label='Messwerte')

# Achsenbeschriftung
plt.xlabel(r'$(1+1/V)$')
plt.ylabel(r"$g' \:/\: cm$")

# in matplotlibrc leider (noch) nicht möglich
plt.grid()
plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

# Speicherort
plt.savefig('plot_abbe_g.pdf')
plt.clf()

## Plot b'
print("Plot nach Abbe für b")

# Plot der Ausgleichsgerade
b_linspace = np.linspace(np.min(1+V),np.max(1+V),100)
plt.plot(b_linspace, f(b_linspace,*params_b), 'k-', label="Ausgleichsgerade")

# Plot der Daten
plt.plot((1+V), b, 'ro', label='Messwerte')

# Achsenbeschriftung
plt.xlabel(r"$(1+V)$")
plt.ylabel(r"$b' \:/\: cm$")

# in matplotlibrc leider (noch) nicht möglich
plt.grid()
plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

# Speicherort
plt.savefig('plot_abbe_b.pdf')