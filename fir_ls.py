# fir_design.py: demo of the FIR filter design functions
# to be run per line (e.g., using vscode)

###############################################################################
# methods to design FIR filters
# 1. windowed method
# 2. least-squares method
# 3. Parks-McClellan method
# 4. Linear programming method
###############################################################################

# 2. least-squares method
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

numtaps = 43

fs = 200
f1 = 15
f2 = 30

bands = np.array([0, f1, f1, f2, f2, 0.5*fs])
desired = np.array([1,  1,  1,  0,  0,    0])

wts1 = None
wts2 = [100, .01, 1]

for wts in [wts1, wts2]:
    taps = signal.firls(numtaps, bands, desired, weight=wts, fs=fs)
    w, h = signal.freqz(taps, worN=8000)
    w *= 0.5*fs/np.pi
    plt.subplot(311)

    for band, des in zip(bands.reshape(-1, 2), desired.reshape(-1, 2)):
        plt.plot(band, des, 'k', alpha=0.1, linewidth=4)
    plt.plot(w, np.abs(h), alpha=0.9, label=str(wts))
    plt.legend()
    plt.title('Least Squares Filter Design with different weight', fontsize=10)

    plt.subplot(312)
    for band, des in zip(bands.reshape(-1, 2), desired.reshape(-1, 2)):
        plt.plot(band, des, 'k', alpha=0.1, linewidth=4)
    plt.plot(w, np.abs(h), alpha=0.9)
    plt.xlim(0, 1.1*f1)
    plt.ylim(0.985, 1.015)

    plt.subplot(313)
    for band, des in zip(bands.reshape(-1, 2), desired.reshape(-1, 2)):
        plt.plot(band, des, 'k', alpha=0.1, linewidth=4)
    plt.plot(w, np.abs(h), alpha=0.9)
    plt.ylim(-0.002, 0.02)
    plt.xlim(0.87*f2, 0.5*fs)

plt.show()
