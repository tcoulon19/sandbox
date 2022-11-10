import numpy as np
import matplotlib.pyplot as plt


def generate_wave(sampling_frequency, time_duration, wave_frequency, snr_dB):

    time_step = 1 / sampling_frequency
    time_range = np.arange(-time_duration/2, time_duration/2, time_step)
    sampled_wave = np.sin(2 * np.pi * wave_frequency * time_range)
    sampled_wave = add_noise(sampled_wave, snr_dB)

    return (time_range, sampled_wave)


def add_noise(signal, snr_dB):

    snr = 10 ** (snr_dB / 10)
    noise = np.random.randn(len(signal))
    sum_signal_squared = np.sum(signal ** 2)
    sum_noise_squared = np.sum(noise ** 2)
    alpha = np.sqrt(sum_signal_squared / (snr * sum_noise_squared)) #alpha amplifies noise to meet SNR requirement
    signal_with_noise = signal + alpha * noise

    return signal_with_noise


def generate_sinc(sampling_frequency, time_duration, cutoff_frequency):

    time_step = 1 / sampling_frequency
    time_range = np.arange(-time_duration / 2, time_duration / 2, time_step)
    sampled_wave = 2*cutoff_frequency*np.sinc(2 * cutoff_frequency * time_range)

    return (time_range, sampled_wave)


def calculate_fft(sampled_wave, sampling_frequency, fft_size):

    dft = np.fft.fft(sampled_wave, fft_size)
    dft_real_im = np.fft.fftshift(dft)
    fft_values = abs(dft_real_im) / fft_size

    frequency_resolution = sampling_frequency / fft_size
    frequencies_to_plot = np.arange(-(fft_size * frequency_resolution) // 2, (fft_size * frequency_resolution) // 2, \
        frequency_resolution)
    
    return (fft_values, frequencies_to_plot, dft_real_im)


def multiply_ffts(dft_real_im_wave, dft_real_im_sinc, fft_size, fs):

    fft_both = dft_real_im_wave*dft_real_im_sinc
    abs_fft_both = abs(fft_both)
    filtered_wave = fft_size*np.fft.ifft((np.fft.ifftshift(fft_both)), n=fft_size)
    time_range_recomp = np.arange(-len(filtered_wave)/2, len(filtered_wave)/2)/fs

    return (abs_fft_both, filtered_wave, time_range_recomp)


#Inputs
sampling_frequency = 200000 #Hz
time_duration = .01 #s
center_frequency = 1000 #Hz
cutoff_frequency = 2000 #Hz
snr_dB = 20 #dB
fft_size = 2000


(time_range, sampled_wave) = generate_wave(sampling_frequency, time_duration, center_frequency, snr_dB)
(time_range, sampled_sinc) = generate_sinc(sampling_frequency, time_duration, cutoff_frequency)
(sine_wave_fft, frequencies_to_plot_1, dft_real_im_wave) = calculate_fft(sampled_wave, sampling_frequency, fft_size)
(sinc_fft, frequencies_to_plot_2, dft_real_im_sinc) = calculate_fft(sampled_sinc, sampling_frequency, fft_size)
(fft_both, filtered_wave, time_range_recomp) = multiply_ffts(dft_real_im_wave, dft_real_im_sinc, fft_size, sampling_frequency)


plt.figure(0)
plt.plot(time_range, sampled_wave)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Sine wave with noise")
plt.savefig("filter_example_images/sine_wave_with_noise.png")

plt.figure(1)
plt.plot(time_range, sampled_sinc)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Sinc time domain")
plt.savefig("filter_example_images/sinc_time_domain.png")

plt.figure(2)
plt.plot(frequencies_to_plot_1, sine_wave_fft)
plt.xlabel("Frequency (Hz)")
plt.title("FFT sine wave with noise")
plt.xlim(-3*cutoff_frequency,3*cutoff_frequency)
plt.savefig("filter_example_images/fft_sine_wave_with_noise.png")

plt.figure(3)
plt.plot(frequencies_to_plot_2, sinc_fft)
plt.xlabel("Frequency (Hz)")
plt.title("FFT sinc")
plt.xlim(-3*cutoff_frequency,3*cutoff_frequency)
plt.savefig("filter_example_images/fft_sinc.png")

plt.figure(4)
plt.plot(frequencies_to_plot_2, fft_both)
plt.xlabel("Frequency (Hz)")
plt.title("FFT multiplied")
plt.xlim(-3*cutoff_frequency,3*cutoff_frequency)
plt.savefig("filter_example_images/fft_multiplied.png")

plt.figure(5)
plt.plot(time_range_recomp, filtered_wave)
plt.xlabel("Time (s)")
plt.ylabel('Amplitude (V)')
plt.title("Filtered wave")
plt.savefig("filter_example_images/filtered_wave.png")
