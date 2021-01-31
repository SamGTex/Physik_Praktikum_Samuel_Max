import numpy as np
from uncertainties import ufloat
r = ufloat(10,1)
r = r/100
R = ufloat(15,1)
R = R/100
h = ufloat(20,1)
h = h/100

print(np.pi* R**2 *h-np.pi* r**2 *h)