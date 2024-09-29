import numpy as np
import matplotlib.pyplot as plt

# Parameters for the known signal (sine wave)
frequency = 5  # Frequency in Hz
sampling_rate = 150  # Samples per second
signal_length = 500  # Number of samples
t = np.arange(0, signal_length) / sampling_rate  # Time vector

# Generate a sine wave signal
signal =  np.sin(2 * np.pi * frequency * t)

autocorr = np.correlate(signal, signal, mode='full')

autocorr = autocorr / np.max(autocorr)

# Define the lag axis
lags = np.arange(-signal_length + 1, signal_length)

# Plot the signal
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Sine Wave Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')

# Plot the autocorrelation
plt.subplot(2, 1, 2)
plt.plot(lags / sampling_rate, autocorr)
plt.title('Autocorrelation of the Sine Wave')
plt.xlabel('Lag (seconds)')
plt.ylabel('Autocorrelation')

plt.tight_layout()
plt.show()
