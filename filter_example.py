import numpy as np
import matplotlib.pyplot as plt

def generate_sinc(sampling_frequency, time_duration, center_frequency):

    time_step = 1 / sampling_frequency
    time_range = np.arange(-time_duration // 2, time_duration // 2, time_step)
    sampled_wave = np.sin(2 * np.pi * center_frequency * time_range) / (2 * np.pi * center_frequency * time_range)

    return (time_range, sampled_wave)

#Inputs
sampling_frequency = 200000 #Hz
time_duration = .01 #s
wave_frequency = 1000 #Hz

(time_range, sampled_wave) = generate_sinc(sampling_frequency, time_duration, wave_frequency)

plt.figure(0)
plt.plot(time_range, sampled_wave)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Voltage vs. Time")
plt.savefig("sinc_time_domain.png")