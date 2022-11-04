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


def mulitply_ffts(dft_real_im_wave, dft_real_im_sinc, time_range):

    fft_both = np.multiply(dft_real_im_wave,dft_real_im_sinc)
    abs_fft_both = abs(fft_both)
    filtered_wave = abs(np.fft.ifft((np.fft.ifftshift(fft_both)), n=len(time_range)))

    return (abs_fft_both, filtered_wave)


#Inputs
sampling_frequency = 2000000 #Hz
time_duration = .01 #s
center_frequency = 1000 #Hz
cutoff_frequency = 2000 #Hz
snr_dB = 20 #dB
fft_size = 200000


(time_range, sampled_wave) = generate_wave(sampling_frequency, time_duration, center_frequency, snr_dB)
(time_range, sampled_sinc) = generate_sinc(sampling_frequency, time_duration, cutoff_frequency)
(sine_wave_fft, frequencies_to_plot_1, dft_real_im_wave) = calculate_fft(sampled_wave, sampling_frequency, fft_size)
(sinc_fft, frequencies_to_plot_2, dft_real_im_sinc) = calculate_fft(sampled_sinc, sampling_frequency, fft_size)

plt.figure(0)
plt.plot(time_range, sampled_wave)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Sine wave with noise")
plt.xlim(-time_duration/4, time_duration/4)
plt.savefig("sine_wave_with_noise.png")

plt.figure(1)
plt.plot(time_range, sampled_sinc)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Sinc time domain")
plt.xlim(-time_duration/4, time_duration/4)
plt.savefig("sinc_time_domain.png")

plt.figure(2)
plt.plot(frequencies_to_plot_1, sine_wave_fft)
plt.xlabel("Frequency (Hz)")
plt.title("FFT sine wave with noise")
plt.xlim(-3*cutoff_frequency,3*cutoff_frequency)
plt.savefig("fft_sine_wave_with_noise.png")

plt.figure(3)
plt.plot(frequencies_to_plot_2, sinc_fft)
plt.xlabel("Frequency (Hz)")
plt.title("FFT sinc")
plt.xlim(-3*cutoff_frequency,3*cutoff_frequency)
plt.savefig("fft_sinc.png")


(fft_both, filtered_wave) = mulitply_ffts(dft_real_im_wave, dft_real_im_sinc, time_range)

plt.figure(4)
plt.plot(frequencies_to_plot_2, fft_both)
plt.xlabel("Frequency (Hz)")
plt.title("FFT multiplied")
plt.xlim(-3*cutoff_frequency,3*cutoff_frequency)
plt.savefig("fft_multiplied.png")

plt.figure(5)
plt.plot(time_range, filtered_wave)
plt.xlabel("Time (s)")
plt.ylabel('Amplitude (V)')
plt.title("Filtered wave")
plt.xlim(-time_duration/4, time_duration/4)
plt.ylim(-2,2)
plt.savefig("filtered_wave.png")
