import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy.signal import find_peaks

N, T1, T2, T3, T4, T5, T6, T7, T8, s = (np.genfromtxt('data/dynamisch1.txt', delimiter=', ', unpack=True))
T1 = T1
T2 = T2
s = s

#minima finden
#x werte der minima ausgeben

T1x_mini = find_peaks(-T1)
T2x_mini = find_peaks(-T2)
T1x_mini = T1x_mini[0]
T1x_mini= T1x_mini[1:]
T2x_mini = T2x_mini[0]

#maxima finden

T1x_max = find_peaks(T1)
T2x_max = find_peaks(T2)
T1x_max = T1x_max[0]
T2x_max = T2x_max[0]
T1_max = T1[T1x_max]
T2_max = T2[T2x_max]

print('T1 Minima : ', T1x_mini)
print('T2 Minima : ', T2x_mini)
print('T1 Maxima : ', (T1x_max,T1_max),  'T2 Maxima : ', T2x_max)

#y werte der minima finden

T1_mini, T2_mini = [], []
T1_mini = T1[T1x_mini]
T2_mini = T2[T2x_mini]
f = interp1d(T1x_mini, T1_mini,  fill_value="extrapolate")
f2 = interp1d(T2x_mini, T2_mini,  fill_value="extrapolate")
y1_mini = f(s)
y2_mini = f2(s)
print(y1_mini[T1x_max], T1_max)

#werte berechnen

print('Amplituden abstände T1: ',T1_max - y1_mini[T1x_max])
print('Amplituden abstände T2: ', T2_max - y2_mini[T2x_max])
#plots machen

plt.xlabel(r'$t \, / \, s$')
plt.ylabel(r'$T \, / \, °C$')
plt.grid()
plt.plot(s, T1, 'g-', label='T1')
plt.plot(s, T2, 'r-', label='T2')
#plt.plot(s, y1_mini, '--', label='Interpolation T1')
#plt.plot(s, y2_mini, '--', label='Interpolation T2')
plt.legend(loc='best')
plt.savefig('dynamisch_T1_T2.pdf')
plt.show