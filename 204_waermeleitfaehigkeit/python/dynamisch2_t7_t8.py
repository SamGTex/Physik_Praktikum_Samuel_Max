import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy.signal import find_peaks

N, T1, T2, T3, T4, T5, T6, T7, T8, s = (np.genfromtxt('data/dynamisch2.txt', delimiter=', ', unpack=True))
T7 = T7
T8 = T8
s = s
T7 = T7
T8 = T8
s = s

#minima finden
#x werte der minima ausgeben

T7x_mini = find_peaks(-T7)
T8x_mini = find_peaks(-T8)
T7x_mini = T7x_mini[0]
T7x_mini= T7x_mini[1:]
T8x_mini = T8x_mini[0]
T8x_mini = T8x_mini[]



#maxima finden

T7x_max = find_peaks(T7)
T8x_max = find_peaks(T8)
T7x_max = T7x_max[0]
T8x_max = T8x_max[0]
T7_max = T7[T7x_max]
T8_max = T8[T8x_max]



#y werte der minima finden

T7_mini, T8_mini = [], []
T7_mini = T7[T7x_mini]
T8_mini = T8[T8x_mini]
f = interp1d(T7x_mini, T7_mini,  fill_value="extrapolate")
f2 = interp1d(T8x_mini, T8_mini,  fill_value="extrapolate")
y1_mini = f(s)
y2_mini = f2(s)
print(y2_mini)
#werte berechnen
print('T7 Minima : ', (T7x_mini ,T7_mini))
print('T8 Minima : ', (T8x_mini, T8_mini))
#print('T7 Maxima : ', (T7x_max,T7_max),  'T8 Maxima : ', (T8x_max, T8_max))
#print('Amplituden abstände T7: ',T7_max - y1_mini[T7x_max])
#print('Amplituden abstände T8: ', T8_max - y2_mini[T8x_max])
#plots machen
print(y1_mini)
plt.xlabel(r'$t \, / \, s$')
plt.ylabel(r'$T \, / \, °C$')
plt.grid()
plt.plot(s, T7, 'g-', label='T7')
plt.plot(s, T8, 'r-', label='T8')
plt.plot(s, y1_mini, '--', label='Interpolation T7')
plt.plot(s, y2_mini, '--', label='Interpolation T8')
plt.legend(loc='best')
plt.savefig('dynamisch_T7_T8.pdf')
plt.show()

