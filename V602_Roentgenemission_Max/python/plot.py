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