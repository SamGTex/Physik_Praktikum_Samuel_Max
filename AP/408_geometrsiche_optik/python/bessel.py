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

e, b, g = (np.genfromtxt('data/weiss_bessel.csv', delimiter=', ', unpack=True))
d = g-b
f = (e**2 - d**2)/(4*e)
print(f)

f_mean = ufloat(np.mean(f), stats.sem(f))
print(f_mean)

e_rot, b_rot = (np.genfromtxt('data/rot_bessel.csv', delimiter=', ', unpack=True))
g_rot = e_rot - b_rot
d_rot = g_rot - b_rot

f_rot = (e_rot**2 -d_rot**2)/(4*e_rot)
print('Brennweite rotes licht', f_rot)

f_mean_rot = ufloat(np.mean(f_rot), stats.sem(f_rot))
print('Mittelwert rote Brennweite : ',f_mean_rot)

e_blau, b_blau = (np.genfromtxt('data/blau_bessel.csv', delimiter=', ', unpack=True))
g_blau = e_blau - b_blau
d_blau = g_blau - b_blau

f_blau = (e_blau**2 -d_blau**2)/(4*e_blau)
print('Brennweite blaues licht', f_blau)
f_mean_blau = ufloat(np.mean(f_blau), stats.sem(f_blau))
print('Mittelwert blaue Brennweite : ', f_mean_blau)