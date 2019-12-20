import numpy as np
from uncertainties import ufloat
D=ufloat(0.032,0.014)
I_d=ufloat(0.0038,0.0019)
def I(T):
    return T**2*D/(4*np.pi**2)
messung, T = np.genfromtxt('data/zylinder_gr.csv',comments='#',unpack=True,delimiter=',')
T_m = ufloat(T.mean(),T.std(ddof=1))
print('T:',T_m)
print('I:',I(T_m) - I_d)
