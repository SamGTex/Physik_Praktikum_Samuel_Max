import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy.signal import find_peaks
from scipy.stats import sem

theta, R = (np.genfromtxt('data/ComptonAl.txt', delimiter=', ', unpack=True))

d = 201.4 * 10**(-12)
n = 1

lamda = 2*d*np.sin(theta) / n 

