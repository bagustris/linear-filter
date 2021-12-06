# fir demo
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
x = np.random.randn(50)

# taps is the coefficients of the FIR filter
taps = np.array([0.0625, 0.25, 0.375,
                 0.25, 0.0625])

# convolve with mode='same" for maximum length of two
y = np.convolve(x, taps, mode='same')

plt.figure()
plt.subplot(3, 1, 1)
plt.stem(x)
plt.subplot(3, 1, 2)
plt.stem(taps)
plt.subplot(3, 1, 3)
plt.stem(y)

plt.show()
