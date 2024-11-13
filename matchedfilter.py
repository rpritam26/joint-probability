import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create the template signal (e.g., a simple pulse)
def generate_pulse_signal(duration, frequency, sampling_rate):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)  # A sine wave as the template
    return t, signal

# Parameters for the signal
duration = 1.0  # Duration of the pulse signal in seconds
frequency = 5  # Frequency of the signal in Hz
sampling_rate = 1000  # Sampling rate in Hz (samples per second)

# Generate the template pulse signal
t, template_signal = generate_pulse_signal(duration, frequency, sampling_rate)

# Step 2: Simulate a noisy received signal (signal + noise)
# Create noise (Gaussian noise)
noise_level = 0.5  # Standard deviation of the noise
noise = noise_level * np.random.randn(len(t))

# Simulate the received signal (template signal + noise)
received_signal = template_signal + noise

# Plot the noisy received signal and the template signal
plt.figure(figsize=(12, 6))

# Plot the template signal
plt.subplot(2, 1, 1)
plt.plot(t, template_signal, label='Template Signal (Reference)', color='blue')
plt.title('Template Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Plot the received signal with noise
plt.subplot(2, 1, 2)
plt.plot(t, received_signal, label='Received Signal (with Noise)', color='red')
plt.title('Received Signal (with Noise)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# Step 3: Apply the matched filter by correlating the received signal with the template signal
def matched_filter(received_signal, template_signal):
    # Perform the correlation of the received signal with the template (matched filter operation)
    return np.correlate(received_signal, template_signal, mode='same')

# Apply the matched filter
filtered_signal = matched_filter(received_signal, template_signal)

# Step 4: Plot the matched filter output
plt.figure(figsize=(10, 6))
plt.plot(t, filtered_signal, label='Matched Filter Output', color='green')
plt.title('Matched Filter Output')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()

# Step 5: Detect the signal (find the peak of the matched filter output)
peak_index = np.argmax(filtered_signal)
peak_time = t[peak_index]
peak_value = filtered_signal[peak_index]
print(f"Peak detected at time {peak_time:.4f}s with value {peak_value:.4f}")

# Plot the received signal and the matched filter output for comparison
plt.figure(figsize=(12, 6))
plt.plot(t, received_signal, label='Received Signal (with Noise)', color='red')
plt.plot(t, filtered_signal, label='Matched Filter Output', color='green', linewidth=2)
plt.axvline(peak_time, color='black', linestyle='--', label=f"Detected Peak at {peak_time:.4f}s")
plt.title('Received Signal and Matched Filter Output')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
