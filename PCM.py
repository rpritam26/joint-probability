import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency (Hz)
f = 5  # Frequency of the sine wave (Hz)
T = 1  # Duration (seconds)
N = fs * T  # Total number of samples
t = np.linspace(0, T, N, endpoint=False)

# Generate a sine wave
amplitude = 1
sine_wave = amplitude * np.sin(2 * np.pi * f * t)

# Sampling
sampling_rate = 50  # Samples per second
sample_times = np.arange(0, T, 1 / sampling_rate)
sampled_values = amplitude * np.sin(2 * np.pi * f * sample_times)

# Quantization
levels = 8  # Number of quantization levels
quantization_step = 2 * amplitude / levels
quantized_samples = np.round(sampled_values / quantization_step) * quantization_step

# NRZ Line Encoding
def nrz_encoding(samples):
    encoded_signal = []
    for sample in samples:
        if sample > 0:
            encoded_signal.extend([1] * (fs // sampling_rate))
        else:
            encoded_signal.extend([0] * (fs // sampling_rate))
    return np.array(encoded_signal)

encoded_signal = nrz_encoding(quantized_samples)

# Time vectors for plotting
sampled_t = sample_times
encoded_t = np.linspace(0, T, len(encoded_signal))

# Plotting
plt.figure(figsize=(12, 10))

# Original Sine Wave
plt.subplot(3, 1, 1)
plt.title('Original Sine Wave')
plt.plot(t, sine_wave, label='Sine Wave', color='blue', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

# Sampled and Quantized Signal
plt.subplot(3, 1, 2)
plt.title('Sampled and Quantized Signal')
plt.plot(t, sine_wave, label='Original Sine Wave', color='blue', alpha=0.5, linewidth=2)
plt.scatter(sampled_t, sampled_values, color='red', label='Sampled Values', zorder=5)
plt.step(sampled_t, quantized_samples, where='post', label='Quantized Samples', color='orange', alpha=0.7, linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend(loc='upper right', bbox_to_anchor=(1, 1), bbox_transform=plt.gca().transAxes)

# NRZ Line Encoded Signal
plt.subplot(3, 1, 3)
plt.title('NRZ Line Encoded Signal')
plt.plot(encoded_t, encoded_signal, label='NRZ Encoded Signal', color='green', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Encoded Value')
plt.ylim(-0.5, 1.5)
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
