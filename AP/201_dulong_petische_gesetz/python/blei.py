import numpy as np
from uncertainties import ufloat
from scipy import stats

#Werte
cm = 163.75650422535293 #J/K
c_w = 4.18 * 10**(3) #J/Kg*K
m_p, m_d, m_dg, T_p, T_d, T_m =  np.genfromtxt('data/blei.csv', comments='#', unpack=True, delimiter=',')
rho = 11.35*10**3 #kg/m^3
M = 207.2*10**(-3) #kg/Mol
a = 29*10**(-6) #1/K
k = 42*10**9 #N/m^2
T_p = T_p + 273.15
T_d = T_d + 273.15
T_m = T_m + 273.15
R = 8.314

#Rechnung
m_d2 = m_d - m_dg #masse des Wassers
c_k = (c_w*m_d2 + cm)*(T_m - T_d) / (m_p*(T_p-T_m))
c_k_mittel = ufloat(np.mean(c_k), stats.sem(c_k))
c_v = c_k * M - 9 * a**2 * k * (M/rho) * T_m
c_v_mittel = ufloat(np.mean(c_v), stats.sem(c_v))

#Ausgabe
print('Blei: c_k =', c_k/1000, 'J/g*K')
print('c_k_mittel =', c_k_mittel/1000)
print('c_v =',c_v)
print('c_v_mittel =',c_v_mittel)
print('3R =',3*R)
print('rel. Abweichung:', (c_v_mittel-3*R)*100/(3*R), '%')