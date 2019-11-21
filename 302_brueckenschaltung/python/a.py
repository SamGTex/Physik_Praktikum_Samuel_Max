import csv
import matplotlib.pyplot as plt
import numpy as np

print('Für Rx = Wert 10')
with open('daten/a_10.csv' ) as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    header_row=next(reader)
    r2, r3, r4 = [], [], []
    for row in reader:
        r2.append(row[0])
        r3.append(row[1])
        r4.append(row[2])
    w2=np.array(r2,dtype=int)
    w3=np.array(r3,dtype=int)
    w4=np.array(r4,dtype=int)
    wx=w2*w3/w4
    print('R2:',w2)
    print('R3:',w3)
    print('R4:',w4)
    print('Rx:',wx)
    print('Mittelwert:',np.mean(wx))
    print('Standardabweichung:',np.std(wx, ddof=1))

print('Für Rx = Wert 12')
with open('daten/a_12.csv' ) as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    header_row=next(reader)
    r2, r3, r4 = [], [], []
    for row in reader:
        r2.append(row[0])
        r3.append(row[1])
        r4.append(row[2])
    w2=np.array(r2,dtype=int)
    w3=np.array(r3,dtype=int)
    w4=np.array(r4,dtype=int)
    wx=w2*w3/w4
    print('R2:',w2)
    print('R3:',w3)
    print('R4:',w4)
    print('Rx:',wx)
    print('Mittelwert:',np.mean(wx))
    print('Standardabweichung:',np.std(wx, ddof=1))