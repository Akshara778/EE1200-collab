import numpy as np
import matplotlib.pyplot as plt

# Create frequency range (log scale)
#omega = np.arange(1e-1, 1e-5, 1000)  # rad/s from 0.01 to 100
omega = np.arange(1, 1e10, 10000)
#omega = np.linspace(1, 1000000, 1000)  # rad/s from 0.1 to 100000
# Define parameters
R = 1e3  # ohms
C = 1e-9  # farads

H = 1/(1+ (omega*R*C)**2)


frequencies = np.array([50, 100, 200, 500, 1500, 5000, 20000, 40000, 80000, 200000, 500000])
hipass = np.array([5/5, 5/5, 5/5, 5/5, 5/5, 5/5, 5/5, 5/5, 2.4/5, 1/5, 0.2/5])
w = 2*np.pi*frequencies


#plt.figure()
#plt.scatter(np.log10(w), 20*np.log10(hipass), color='r')
#plt.plot(np.log10(omega), 20*np.log10(H))  # log scale f`or frequency
#plt.grid(True)
#plt.xlabel('Frequency (rad/s) - log scale')
#plt.ylabel('Magnitude (dB)')
#plt.title('Bode Plot - Low Pass Filter')
#plt.show()


#R = 15e3
#frequencies = np.array([300, 500, 1000, 2000, 5000, 10000, 20000, 40000, 50000, 80000])
#lopass = np.array([0.007/5.6, 0.0104/5.6, 0.04/5.6, 0.152/6, 0.8/6.4, 2.2/6.4 ,3.8/6.4, 4.4/6.4, 4.6/6.4, 5/6])
#w = 2*np.pi*frequencies
#
#H = (omega * R * C)**2/(1+ (omega*R*C)**2)
#plt.figure()
#plt.plot(np.log10(omega), 20*np.log10(H))  # log scale for frequency
#plt.scatter(np.log10(w), 20*np.log10(lopass), color='r')
#plt.grid(True)
#plt.xlabel('Frequency (rad/s) - log scale')
#plt.ylabel('Magnitude (dB)')
#plt.title('Bode Plot - High Pass Filter')
#plt.show()



frequencies = np.array([5000, 10000, 15000, 30000, 50000, 100000, 200000, 250000]) # beyond this point, output oscillates so it is hard to measure exactly
bandpass = np.array([10/108, 32/100, 52/102, 70/104, 70/104, 54/104, 18/112, 10/112])
w = 2*np.pi*frequencies
print("w-> ", np.log10(w))
print("H-> ", 20*np.log10(bandpass))
R1 = 10e3
R2 = 1e3
C = 1e-9
H =(omega * R1 * C)**2/((1+ (omega*R2*C)**2)*(1+ (omega*R1*C)**2))
plt.figure()
plt.plot(np.log10(omega), 20*np.log10(H))  # log scale for frequency
plt.scatter(np.log10(w), 20*np.log10(bandpass), color='r')
plt.grid(True)
plt.xlabel('Frequency (rad/s) - log scale')
plt.ylabel('Magnitude (dB)')
plt.title('Bode Plot - Band Pass Filter')
plt.show()
