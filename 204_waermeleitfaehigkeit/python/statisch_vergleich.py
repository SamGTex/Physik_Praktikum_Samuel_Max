import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
N, T1, T2, T3, T4, T5, T6, T7, T8, s = (np.genfromtxt('data/statisch.txt', delimiter=', ', unpack=True))
T1 = T1[:117]
T2 = T2[:117]
T4 = T4[:117]
T5 = T5[:117]
T7 = T7[:117]
T8 = T8[:117]
s = s[:117]
i = [10, 30, 50, 70, 90]
#def diff(m):
#    return T2[m] - T1[m]
#def diff2(m):
#    return T8[m]- T7[m]
for m in i:
    print('Zeitpunkt für m = ', m, 'ist s = ', s[m])
    print('für m = ', m, 'ergibt sich bei T1 und T2: ')
    print(-100*48*10**-6 *(T2[m] - T1[m])/0.03)
    print('für m = ', m , 'ergibt sich bei T7 und T8: ')
    print(-20*48*10**-6 *(T7[m] - T8[m])/0.03)




plt.xlabel(r'$t \, / \, s$')
plt.ylabel(r'$T_{dif} \, / \, °C$')
plt.grid()
plt.plot(s, T2 - T1, 'g-', label='T2 - T1')
plt.plot(s, T7 - T8, 'r-', label='T7 - T8')
plt.legend(loc='best')
plt.savefig('statsisch_vergleich.pdf')
plt.show()