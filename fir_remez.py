###############################################################################
# methods to design FIR filters
# 1. windowed method
# 2. least-squares method
# 3. Parks-McClellan method
# 4. Linear programming method
###############################################################################

# 3. Parks-McClellan method based on the Remez exchange algorithm
from __future__ import division, print_function

import numpy as np
from scipy.signal import remez, freqz
import matplotlib.pyplot as plt


fs = 2000

bands = [0, 250, 350, 550, 700, 0.5*fs]
desired = [0, 1, 0]


for numtaps in [31, 47]:
    weights1 = [1, 1, 1]
    taps = remez(numtaps, bands, desired, weights1, fs=fs)

    w, h = freqz(taps, worN=8000)
    w *= 0.5*fs/np.pi

    weights2 = [1, 25, 1]
    #weights = list(weights1, weights2)
    taps2 = remez(numtaps, bands, desired, weights2, fs=fs)

    w2, h2 = freqz(taps2, worN=8000)
    w2 *= 0.5*fs/np.pi

    plt.figure(figsize=(4.0, 3.0))

    plt.plot(w, np.abs(h), linewidth=1, label='(a)')
    plt.plot(w2, np.abs(h2), linewidth=1, label='(b)')

    rect = plt.Rectangle((bands[1], 0), bands[2]-bands[1], 1.0,
                         facecolor='k',
                         edgecolor='k',
                         alpha=0.075)
    plt.gca().add_patch(rect)
    rect = plt.Rectangle((bands[3], 0), bands[4]-bands[3], 1.0,
                         facecolor='k',
                         edgecolor='k',
                         alpha=0.075)
    plt.gca().add_patch(rect)

    plt.text(10, .9, "%d taps" % numtaps, fontsize=9)

    plt.grid(alpha=0.25)
    plt.legend(loc="center right", framealpha=1, shadow=True)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Gain')
    plt.title("Bandpass filters designed with remez", fontsize=10)
    plt.tight_layout()
    plt.show()
    # plt.savefig("remez_example_%dtaps.pdf" % numtaps)
