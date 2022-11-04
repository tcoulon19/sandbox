import numpy as np
import matplotlib.pyplot as plt

def generate_sinc(sampling_frequency, time_duration, center_frequency):

    time_step = 1 / sampling_frequency
    time_range = np.arange(-time_duration / 2, time_duration / 2, time_step)
    sampled_wave = np.sinc(2 * center_frequency * time_range)

    return (time_range, sampled_wave)

def calculate_fft(sampled_wave, sampling_frequency, fft_size):

    dft = np.fft.fft(sampled_wave, fft_size)
    dft = np.fft.fftshift(dft)
    fft_values = abs(dft) / fft_size

    frequency_resolution = sampling_frequency / fft_size
    frequencies_to_plot = np.arange(-(fft_size * frequency_resolution) // 2, (fft_size * frequency_resolution) // 2, \
        frequency_resolution)

    return (fft_values, frequencies_to_plot)

#Inputs
sampling_frequency = 200000 #Hz
time_duration = .01 #s
center_frequency = 1000 #Hz
fft_size = 20000

(time_range, sampled_wave) = generate_sinc(sampling_frequency, time_duration, center_frequency)
(fft_values, frequencies_to_plot) = calculate_fft(sampled_wave, sampling_frequency, fft_size)

plt.figure(0)
plt.plot(time_range, sampled_wave)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Voltage vs. Time")
plt.savefig("sinc_time_domain.png")

plt.figure(1)
plt.plot(frequencies_to_plot, fft_values)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (V)")
plt.title("Voltage vs Frequency")
plt.xlim(-2*center_frequency,2*center_frequency)
plt.savefig("sinc_freq_domain.png")