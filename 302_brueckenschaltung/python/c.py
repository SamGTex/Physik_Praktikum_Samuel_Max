import csv
import matplotlib.pyplot as plt
import numpy as np

print('Für Lx = Wert 16')
with open('daten/c_16.csv') as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    header_row=next(reader)
    l2, r2, r3, r4 = [], [], [], []
    for row in reader:
        l2.append(row[0])
        r2.append(row[1])
        r3.append(row[2])
        r4.append(row[3])
    w1=np.array(l2,dtype=float)
    w2=np.array(r2,dtype=float)
    w3=np.array(r3,dtype=float)
    w4=np.array(r4,dtype=float)
    rx=w2*w3/w4
    lx=w1*w4/w3
    print('C2:',w1)
    print('R2:',w2)
    print('R3:',w3)
    print('R4:',w4)
    print('Rx:',rx)
    print('Lx:',lx)
    print('Mittelwert Rx:',np.mean(rx))
    print('Standardabweichung Rx:',np.std(rx, ddof=1))
    print('Mittelwert Lx:',np.mean(lx))
    print('Standardabweichung Lx:',np.std(lx, ddof=1))