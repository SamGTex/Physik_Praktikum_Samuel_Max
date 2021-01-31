import numpy as np
from uncertainties import ufloat

#Werte
t = 120 #s
N1 = ufloat(96041,np.sqrt(96041))/t
N2 = ufloat(76518,np.sqrt(76518))/t
N12 = ufloat(158479,np.sqrt(158479))/t

#Rechnung
T = (N1 + N2 - N12) / (2*N1*N2)

print('N12 =',N12,'und N1+N2 =',N1+N2)
print('T =',T)
print('T^2N_1^2 =', T**2*N1**2)
print('T^2N_2^2 =', T**2*N2**2)
print('T^2N_12^2 =', T**2*N12**2)