import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x, U = (np.genfromtxt('data.txt', delimiter= ', ', unpack=True))

D = (x -1) * 6
def func(D, m):
    return(D*m-19.5)

popt, pcov = curve_fit(func, D , U)
print(popt)
print(pcov)


plt.xlabel(r'$D \, / \, mm$')
plt.ylabel(r'$U \, / \, V$')
plt.plot(D, func(D, popt), 'r-', label='lineare Regression')
plt.plot(D, U, 'bo', label='Spannungsverlauf')
plt.legend()
plt.savefig('regression.pdf')
plt.show()

