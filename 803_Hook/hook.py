import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x,D):
    return x*D
x=np.array([58,53,48,43,38,33,28,23,18,13])
F=np.array([1.73,1.58,1.44,1.28,1.13,0.98,0.83,0.68,0.53,0.38])
popt, pcov = curve_fit(func, x/100, F)
print(popt)
plt.plot(x/100,func(x/100,popt),'b-')
plt.plot(x/100,F,'rx')
plt.savefig('plot.pdf')
plt.show()
print('Summe x', np.sum(x/10))
print('Summe x^2', np.sum((x/10)*(x/10)))
print('Summe F', np.sum(F))
print('Summe F*x', np.sum(F*(x/10)))