import numpy as np
import matplotlib.pyplot as plt

fs = 1000000
t = np.arange(-5,5,1/fs)
fft_size = fs*10
g_t = np.sinc(t)

G_f = np.fft.fftshift(np.fft.fft(g_t))
frequency_resolution = fs / fft_size
frequencies_to_plot = np.arange(-(fft_size * frequency_resolution) // 2, (fft_size * frequency_resolution) // 2, frequency_resolution)

plt.figure(0)
plt.plot(t,g_t)
plt.savefig('filter_example_im1.png')

plt.figure(1)
plt.plot(frequencies_to_plot,G_f)
plt.xlim(-3,3)
plt.savefig('filter_example_im2.png')