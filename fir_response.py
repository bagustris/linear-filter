from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

for n in [3, 7, 21]:
    taps = np.full(n, fill_value=1.0 / n)
    w, h = signal.freqz(taps, worN=2000)
    plt.plot(w, abs(h), label='n = %d' % n)
    plt.legend(framealpha=1, shadow=True)

plt.show()
