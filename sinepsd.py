import numpy as np
import matplotlib.pyplot as plt

# Parameters for the known signal (cosine wave)
frequency = 5 # Frequency in Hz
sampling_rate = 150  # Samples per second
signal_length = 500  # Number of samples
t = np.arange(0, signal_length) / sampling_rate  # Time vector

# Generate a sine wave signal
signal = np.sin(2 * np.pi * frequency * t)

# Compute the Fourier Transform of the signal
fft_signal = np.fft.fft(signal)
fft_freqs = np.fft.fftfreq(signal_length, 1/sampling_rate)

# Compute Power Spectral Density (PSD)
psd = np.abs(fft_signal)**2 / signal_length

# Take only the positive half of the frequencies (since FFT is symmetric)
positive_freqs = fft_freqs[:signal_length//2]
positive_psd = psd[:signal_length//2]

# Plot the signal
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Sine Wave Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')

# Plot the Power Spectral Density
plt.subplot(2, 1, 2)
plt.plot(positive_freqs, positive_psd)
plt.title('Power Spectral Density of the Sine Wave')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density (V^2/Hz)')
plt.grid(True)

plt.tight_layout()
plt.show()
