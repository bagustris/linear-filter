# fir_design.py: demo of the FIR filter design functions
# to be run per line (e.g., using vscode)

###############################################################################
# methods to design FIR filters
# 1. windowed method
# 2. least-squares method
# 3. Parks-McClellan method
# 4. Linear programming method
###############################################################################

# 1. windowed method
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

freqs = [0, 48, 60, 72, 150, 175, 1000]
gains = [1, 1, 0.1, 1, 1, 0, 0]

fs = 2000
taps = 185

windows = ['boxcar', 'triang', 'hann', 'hamming', 'bartlett', 'blackman']
# taps = []

for window in windows:
    tap = signal.firwin2(taps, freqs, gains, nyq=.5*fs, window=window)
    win = signal.get_window(window, taps)
    wk, hk = signal.freqz(tap, 1, worN=2000)
    plt.figure(1)
    plt.plot(win, label=window)
    plt.legend()
    plt.figure(2)
    plt.plot(0.5*fs*wk/np.pi, np.abs(hk), label=window)
    plt.xlim(0, 210)
    plt.legend()
plt.show()


# 2. least-squares method

