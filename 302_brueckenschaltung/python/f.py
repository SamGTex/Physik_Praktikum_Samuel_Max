import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
def g(o,u_br):
    z=(o**2-1)**2
    n=9*((1-o**2)**2 + 9*(o**2))
    return (u_br/np.sqrt(z/n))
with open('daten/e.csv' ) as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    header_row=next(reader)
    f, u = [], []
    for row in reader:
        f.append(row[0])
        u.append(row[1])
    indices = [i for i, x in enumerate(f) if x == "160"]
    f=np.array(f,dtype=float)
    u=np.array(u,dtype=float)
    u_br=u[indices]/(2*np.sqrt(2)*1000)
    u_s=1
    print('U_br_eff:',u_br)
    print('U_2:', g(2,u_br))
    print('k:',g(2,u_br)/u_s)

  
   