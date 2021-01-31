import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#funktion
def func(phi,w,rc):
    return -np.sin(phi)/(w*rc)

#daten einlesen
with open('data/phase.csv' ) as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    header_row=next(reader)
    f, U, a, b = [], [], [], []
    for row in reader:
        f.append(row[0])
        U.append(row[1])
        a.append(row[2])
        b.append(row[3])
    f=np.array(f,dtype=float)
    U=np.array(U,dtype=float)
    a=np.array(a,dtype=float)
    b=np.array(b,dtype=float)

#werte
U0=0.6
phi=(a/b)*2*np.pi

#plots
x=np.linspace(np.min(phi),np.max(phi),100)
plt.subplot(111,projection='polar')
plt.plot(phi,U/U0,'rx')
plt.plot(x,np.cos(x),'b-')
plt.savefig('plotd.pdf')
plt.show()