import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x,D):
    return x*D
x=np.array([58,53,48,43,38,33,28,23,18,13,8,3])
F=np.array([1.73,1.58,1.44,1.28,1.13,0.98,0.83,0.68,0.53,0.38,0.24,0.09])

popt, pcov = curve_fit(func, x, F)
plt.plot(x,func(x,popt),'b-')
plt.plot(x,F,'rx')
plt.show()
plt.savefig('plot.pdf')