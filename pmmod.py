import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert

# Parameters
Am = 1          # Amplitude of message signal
fm = 50         # Frequency of message signal (Hz)
fc = 500        # Carrier frequency (Hz)
Ac = 1          # Amplitude of carrier signal
kp = 2 * np.pi  # Phase sensitivity (Modulation index)
Fs = 10000      # Sampling frequency (Hz)
t = np.linspace(0, 0.1, int(0.1 * Fs))  # Time vector

# Message Signal (sinusoidal)
message = Am * np.cos(2 * np.pi * fm * t)

# Phase Modulated Signal (PM)
modulated_signal = Ac * np.cos(2 * np.pi * fc * t + kp * message)

# Additive White Gaussian Noise (AWGN)
noise_amplitude = 0.5
noise = noise_amplitude * np.random.normal(0, 1, modulated_signal.shape)

# Signal with Noise
modulated_signal_with_noise = modulated_signal + noise

# PM Demodulation using the Hilbert transform (Instantaneous phase extraction)
analytic_signal = hilbert(modulated_signal_with_noise)
instantaneous_phase = np.unwrap(np.angle(analytic_signal))

# Removing the carrier's phase
demodulated_signal = (instantaneous_phase - 2 * np.pi * fc * t) / kp

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
plt.title("PM Modulated Signal (Without Noise)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Modulated signal with noise
plt.subplot(4, 1, 3)
plt.plot(t, modulated_signal_with_noise)
plt.title("PM Modulated Signal (With Noise)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Demodulated signal
plt.subplot(4, 1, 4)
plt.plot(t, demodulated_signal)
plt.title("Demodulated Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
