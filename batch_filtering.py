# pada contoh sebelumnya kita telah belajar
# memfilter satu sinyal dengan FIR filter
# Bagaimana jika kita ingin memfilter banyak filter bersamaan?

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def butter_bandpass(lowcut, highcut, fs, order):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    sos = signal.butter(order, [low, high], btype='band',
                        output='sos')
    return sos


def make_data(T, fs):
    """
    Function to make data
    args:
        T: time
        fs: sampling rate
    return:
        t: number of samples
        x: data
    """
    nsamples = int(T * fs)
    t = np.linspace(0, T, nsamples, endpoint=False)
    a = 0.025
    f0 = 550.0
    x = 0.07 * np.sin(2 * np.pi * 1.2 * np.sqrt(t))
    x += 0.01 * np.cos(2 * np.pi * 312 * t + 0.1)
    x += a * np.cos(2 * np.pi * f0 * t + .11)
    x += 0.03 * np.cos(2 * np.pi * 2000 * t)
    return t, x


# Sample rate and desired cutoff frequencies (in Hz).
fs = 4800.0
lowcut = 400.0
highcut = 1200.0

# total time of data
T = 0.06
t, x = make_data(T, fs)

sos = butter_bandpass(lowcut, highcut, fs, 12)

batch_size = 72

# Array of initial conditions for the SOS filter.
z = np.zeros((sos.shape[0], 2))

# Preallocate space for the filtered signal.
y = np.empty_like(x)

# for debugging
# plt.plot(t, x, label='data')
# plt.show()

# divide data into batches
start = 0
while start < len(x):
    stop = min(start + batch_size, len(x))
    y[start:stop], z = signal.sosfilt(sos, x[start:stop], zi=z)
    start = stop


plt.figure(figsize=(4.0, 3.2))

plt.plot(t, x, 'k', alpha=0.4, linewidth=1, label='Noisy signal')
# plt.show()

start = 0
alpha = 0.5
while start < len(x):
    stop = min(start + batch_size, len(x))
    if start == batch_size:
        label = 'Filtered signal'
    else:
        label = None
    plt.plot(t[start:stop+1], y[start:stop+1], 'C0', alpha=alpha, label=label)
    alpha = 1.5 - alpha
    start = stop

plt.xlabel('Time (seconds)')
plt.grid(alpha=0.5)
plt.axis('tight')
plt.xlim(0, T)
plt.legend(framealpha=1, shadow=True, loc='upper left')
plt.tight_layout()
# plt.savefig("bandpass_batch_example.pdf")
plt.show()
