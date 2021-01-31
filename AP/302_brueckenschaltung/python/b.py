import csv
import matplotlib.pyplot as plt
import numpy as np

print('Für Cx = Wert 19')
with open('daten/b_19.csv' ) as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    header_row=next(reader)
    c2, r2, r3, r4 = [], [], [], []
    for row in reader:
        c2.append(row[0])
        r2.append(row[1])
        r3.append(row[2])
        r4.append(row[3])
    w1=np.array(c2,dtype=int)
    w2=np.array(r2,dtype=int)
    w3=np.array(r3,dtype=int)
    w4=np.array(r4,dtype=int)
    rx=w2*w3/w4
    cx=w1*w4/w3
    print('C2:',w1)
    print('R2:',w2)
    print('R3:',w3)
    print('R4:',w4)
    print('Rx:',rx)
    print('Cx:',cx)
    print('Mittelwert Rx:',np.mean(rx))
    print('Standardabweichung Rx:',np.std(rx, ddof=1))
    print('Mittelwert Cx:',np.mean(cx))
    print('Standardabweichung Cx:',np.std(cx, ddof=1))