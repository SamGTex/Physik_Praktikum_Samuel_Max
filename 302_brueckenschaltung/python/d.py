import csv
import matplotlib.pyplot as plt
import numpy as np

print('Für Cx = Wert 19')
with open('daten/d_19.csv' ) as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    header_row=next(reader)
    r2, c4, r3, r4 = [], [], [], []
    for row in reader:
        r2.append(row[0])
        c4.append(row[1])
        r3.append(row[2])
        r4.append(row[3])
    r2=np.array(r2,dtype=int)
    c4=np.array(c4,dtype=int)
    r3=np.array(r3,dtype=int)
    r4=np.array(r4,dtype=int)
    rx=(r2*r3)/r4
    lx=r2*r3*c4
    print('R2:',r2)
    print('C4:',c4)
    print('R3:',r3)
    print('R4:',r4)
    print('Rx:',rx)
    print('Lx:',lx)
    print('Mittelwert Rx:',np.mean(rx))
    print('Standardabweichung Rx:',np.std(rx, ddof=1))
    print('Mittelwert Lx:',np.mean(lx))
    print('Standardabweichung Lx:',np.std(lx, ddof=1))