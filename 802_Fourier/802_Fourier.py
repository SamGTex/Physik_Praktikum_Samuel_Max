import numpy as np

T = np.pi
for k in range(17):
    print(4/(np.pi-4*k**2*np.pi))

#obere = 2/T * (np.sign(np.sin(T/2)) * (w * np.sin(T/2) * np.sin(w * T/2) 
# + np.cos(T/2) * np.cos(w * T/2))) / (w**2 - 1)
#
#   untere = 2/T * (np.sign(np.sin(-T/2)) * (w * np.sin(-T/2) * np.sin(w * (-T/2)) 
#  + np.cos(-T/2) * np.cos(w * (-T/2)))) / (w**2 - 1) https://www.onlinemathe.de/forum/Fourier-Reihe-sinx