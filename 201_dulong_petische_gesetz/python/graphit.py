import numpy as np
from uncertainties import ufloat
from scipy import stats
cm = 163.75650422535267
c_w=4.18
m_p, m_d, m_dg, T_p, T_d, T_m =  np.genfromtxt('data/graphit.csv', comments='#', unpack=True, delimiter=',')

m_d2 = m_d - m_dg #masse des Wassers

c_k = (c_w*m_d + cm)*(T_m - T_d) / (m_p*(T_p-T_m))
c_k_mittel = ufloat(np.mean(c_k), stats.sem(c_k))
print('Graphit: c_k =', c_k, 'J/g*K')
print('c_k_mittel =', c_k_mittel)