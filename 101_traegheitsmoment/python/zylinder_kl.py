import numpy as np
from uncertainties import ufloat

D=ufloat(0.032,0.014)
I_d=ufloat(0.0038,0.0019)

def I(T):
    return T**2*D/(4*np.pi**2)

messung, T = np.genfromtxt('data/zylinder_kl.csv',comments='#',unpack=True,delimiter=',')
T_m = ufloat(T.mean(),T.std(ddof=1))
r=3.75/100 #m
h=3/100 #m
m=1.180 #kg

I_ex=I(T_m)
I_th=m*(r**2/4 + h**2/12)
I_diff=I_th-I_ex
print('T_mittel:',T_m)
print('I_ex =', I_ex)
print('I_th =', I_th)
print('I_diff =', I_diff, '(',I_diff*100/I_th,'% )')
print('I_diff(mit I_d) =', I_diff-I_d, '(',(I_diff-I_d)*100/I_th,'% )')