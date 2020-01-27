
import numpy as np
from uncertainties import ufloat
from scipy import stats

#Werte
cm = 163.75650422535293 #J/K
c_w = 4.18 * 10**(3) #J/Kg*K
m_p = 151.85 * 10**(-3) #kg
m_d = 821.96 * 10**(-3) #kg
m_dg = 237.84 * 10**(-3) #kg
T_p = 90.0 + 273.15
T_d = 21.4 + 273.15
T_m = 24.6 + 273.15
rho = 2.7*10**3 #kg/m^3
M = 27.0*10**(-3) #kg/Mol
a = 23.5*10**(-6) #1/K
k = 75*10**9 #N/m^2
R = 8.314

#Rechnung
m_d2 = m_d - m_dg #masse des Wassers
c_k = (c_w*m_d2 + cm)*(T_m - T_d) / (m_p*(T_p-T_m))
c_v = c_k * M - 9 * a**2 * k * (M/rho) * T_m

#Ausgabe
print('Aluminium: c_k =', c_k/1000, 'J/g*K')
print('c_v =',c_v)
print('3R =',3*R)
print('rel. Abweichung:', (c_v-3*R)*100/(3*R), '%')