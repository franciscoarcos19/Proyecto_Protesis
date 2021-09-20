import numpy as np
from numpy import array, r_
import matplotlib.pyplot as plt
from scipy.signal import lfilter, resample, firwin, hilbert, butter, sosfilt, iirnotch

sensor1 = np.loadtxt('C1.txt')
sensor2 = np.loadtxt('C2.txt')
sensor3 = np.loadtxt('C3.txt')
sensor4 = np.loadtxt('C4.txt')
tiempo = np.arange(0,65.000,0.001)
#tiempo = np.arange(0,60.000,0.001)

plt.figure()
plt.plot(tiempo,sensor1)
plt.plot(tiempo,sensor2)
plt.plot(tiempo,sensor3)
plt.plot(tiempo,sensor4)
plt.grid()
#plt.show()

#Aplicacion filtro Butter pasa baja
#b, a = butter(4, 100, 'low', analog=False)
sos = butter(2, 25, 'hp', fs=1000, output='sos')
sensor1_f1 = sosfilt(sos, sensor1)
sensor2_f1 = sosfilt(sos, sensor2)
sensor3_f1 = sosfilt(sos, sensor3)
sensor4_f1 = sosfilt(sos, sensor4)

#Aplicacion filtro Butter pasa alta
sos = butter(10, 300, 'low', fs=1000, output='sos')
sensor1_f2 = sosfilt(sos, sensor1_f1)
sensor2_f2 = sosfilt(sos, sensor2_f1)
sensor3_f2 = sosfilt(sos, sensor3_f1)
sensor4_f2 = sosfilt(sos, sensor4_f1)

#Aplicación filtro Notch
fs = 1000  # Sample frequency (Hz)
f0 = 60.0  # Frequency to be removed from signal (Hz)
Q = 30.0  # Quality factor
# Design notch filter
b,a = iirnotch(f0, Q, fs)
sensor1_f3 = lfilter(b, a, sensor1_f2)
sensor2_f3 = lfilter(b, a, sensor2_f2)
sensor3_f3 = lfilter(b, a, sensor3_f2)
sensor4_f3 = lfilter(b, a, sensor4_f2)

plt.figure()
sensor1_f3[:40]=0
sensor2_f3[:40]=0
sensor3_f3[:40]=0
sensor4_f3[:40]=0
#plt.plot(tiempo,sensor1_f3)
#plt.plot(tiempo,sensor2_f3)
#plt.plot(tiempo,sensor3_f3)
plt.plot(tiempo,sensor4_f3)
plt.grid()
plt.show()