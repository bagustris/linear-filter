import numpy as np

# initialize seed for reproducibility
np.random.seed(123)

# make a random signal
x = np.random.randn(50)

# create taps, array of FIR filter coefficients
taps = np.array([ 0.0625, 0.25, 0.375, 0.25, 0.0625])

# apply filter with convolution
y = np.convolve(x, taps, mode='same')

