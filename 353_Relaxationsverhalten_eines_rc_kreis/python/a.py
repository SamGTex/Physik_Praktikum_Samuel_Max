import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def func(T,RC):
    return np.log(-1/(RC)*T)

with open('data/entladung.csv' ) as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    header_row=next(reader)
    T, U = [], []
    for row in reader:
        T.append(row[0])
        U.append(row[1])
    T=np.array(T,dtype=float)
    U=np.array(U,dtype=float)
U0=0.5
popt, pcov = curve_fit(func, T, np.log(U/U0))
#plt.semilogy(T,U/U0,'rx')
plt.plot(T,func(T,popt),'b-',label='lineare Ausgleichsrechnung')
plt.show()