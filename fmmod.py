import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, find_peaks

# Parameters
Am = 1          # Amplitude of message signal
fm = 50         # Frequency of message signal (Hz)
fc = 500        # Carrier frequency (Hz)
Ac = 1          # Amplitude of carrier signal
beta = 5        # Modulation index
Fs = 10000      # Sampling frequency (Hz)
t = np.linspace(0, 0.1, int(0.1 * Fs))  # Time vector

# Message Signal (sinusoidal)
message = Am * np.cos(2 * np.pi * fm * t)

# Frequency Modulated Signal (FM)
modulated_signal = Ac * np.cos(2 * np.pi * fc * t + beta * np.sin(2 * np.pi * fm * t))

# Additive White Gaussian Noise (AWGN)
noise_amplitude = 0.5
noise = noise_amplitude * np.random.normal(0, 1, modulated_signal.shape)

# Signal with Noise
modulated_signal_with_noise = modulated_signal + noise

# FM Demodulation using numerical differentiation (simple approximation)
instantaneous_phase = np.unwrap(np.angle(hilbert(modulated_signal_with_noise)))
demodulated_signal = np.diff(instantaneous_phase) * Fs / (2 * np.pi * beta)

# Time vector for the demodulated signal (adjusted for diff)
t_demod = t[:-1]

# Plotting
plt.figure(figsize=(12, 8))

# Original message signal
plt.subplot(4, 1, 1)
plt.plot(t, message)
plt.title("Message Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Modulated signal without noise
plt.subplot(4, 1, 2)
plt.plot(t, modulated_signal)
plt.title("FM Modulated Signal (Without Noise)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Modulated signal with noise
plt.subplot(4, 1, 3)
plt.plot(t, modulated_signal_with_noise)
plt.title("FM Modulated Signal (With Noise)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Demodulated signal
plt.subplot(4, 1, 4)
plt.plot(t_demod, demodulated_signal)
plt.title("Demodulated Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
