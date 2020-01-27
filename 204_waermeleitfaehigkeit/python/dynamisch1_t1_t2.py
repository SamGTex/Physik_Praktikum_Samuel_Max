import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy.signal import find_peaks
from scipy.stats import sem

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

#x werte von den minima von alu finden
T5x_mini = find_peaks(-T5)
T6x_mini = find_peaks(-T6)
T5x_mini = T5x_mini[0]
T5x_mini= T5x_mini[1:]
T6x_mini = T6x_mini[0]

#maxima finden

T1x_max = find_peaks(T1)
T2x_max = find_peaks(T2)
T1x_max = T1x_max[0]
T2x_max = T2x_max[0]
T1_max = T1[T1x_max]
T2_max = T2[T2x_max]

#maxima von alu finden

T5x_max = find_peaks(T5)
T6x_max = find_peaks(T6)
T5x_max = T5x_max[0]
T6x_max = T6x_max[0]
T5_max = T5[T5x_max]
T6_max = T6[T6x_max]


#print('T1 Minima : ', T1x_mini)
#print('T2 Minima : ', T2x_mini)
#print('T1 Maxima : ', (T1x_max,T1_max),  'T2 Maxima : ', T2x_max)

#y werte der minima finden

T1_mini, T2_mini = [], []
T1_mini = T1[T1x_mini]
T2_mini = T2[T2x_mini]
f = interp1d(T1x_mini, T1_mini,  fill_value="extrapolate")
f2 = interp1d(T2x_mini, T2_mini,  fill_value="extrapolate")
y1_mini = f(s)
y2_mini = f2(s)
#print(y1_mini[T1x_max], T1_max)

#y werte der minima von alu finden

T5_mini, T6_mini = [], []
T5_mini = T5[T5x_mini]
T6_mini = T6[T6x_mini]
g = interp1d(T5x_mini, T5_mini,  fill_value="extrapolate")
g2 = interp1d(T6x_mini, T6_mini,  fill_value="extrapolate")
y5_mini = g(s)
y6_mini = g2(s)

#werte berechnen

#print('Amplituden abstände T1: ',T1_max - y1_mini[T1x_max])
#print('Amplituden abstände T2: ', T2_max - y2_mini[T2x_max])
print('Amplituden abstände T5: ',T5_max - y5_mini[T5x_max])
print('Amplituden abstände T6: ', T6_max - y6_mini[T6x_max])

#plots machen

plt.xlabel(r'$t \, / \, s$')
plt.ylabel(r'$T \, / \, °C$')
plt.grid()
plt.plot(s, T1, 'g-', label='T1')
plt.plot(s, T2, 'r-', label='T2')
plt.plot(s, y1_mini, '--', label='Interpolation der Minima vonT1')
plt.plot(s, y2_mini, '--', label='Interpolation der Minima von T2')
plt.legend(loc='best')
plt.savefig('dynamisch_T1_T2.pdf')
plt.show

phase = s[T5x_max] - s[T6x_max]
periode = 80
A5 = T5_max - y5_mini[T5x_max]
A6 = T6_max - y6_mini[T6x_max]
#print(np.log(A2/A1))
kappa = (2800 * 830 * (0.03)**2) /(2 * phase * np.log(A6/A5))
print('phase : ', phase)
print('kappa : ', kappa)
print('Messing : ', (np.mean(kappa), sem(kappa)))
