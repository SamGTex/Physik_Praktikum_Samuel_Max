import numpy as np
m_d = (409.74 - 145.80) #g
m_p = (523.55 - 236.60) #g
T_d = 21.6 + 273.15 #K
T_p = 80 + 273.15 #K
T_m = 50 + 273.15 #K
c_w = 4.18

cm = (c_w*m_p*(T_p-T_m) - c_w*m_d*(T_m-T_d)) / (T_m - T_d)
print('c_g*m_g =', cm, 'J/K')