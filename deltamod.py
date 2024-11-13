import numpy as np
import matplotlib.pyplot as plt

# Generate a simple sine wave signal
def generate_sine_wave(frequency, sampling_rate, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)
    return t, signal

# Delta Modulator
def delta_modulate(signal, step_size):
    # Initialize variables
    delta_encoded = []
    previous_sample = 0

    # Perform delta modulation (compare current sample to previous sample)
    for current_sample in signal:
        if current_sample > previous_sample:
            delta_encoded.append(1)  # Output 1 if current sample is higher
            previous_sample += step_size  # Increment previous sample by step size
        else:
            delta_encoded.append(0)  # Output 0 if current sample is lower
            previous_sample -= step_size  # Decrement previous sample by step size
    return np.array(delta_encoded)

# Delta Demodulator (Reconstruct the signal from delta encoded bits)
def delta_demodulate(delta_encoded, step_size, initial_value=0):
    decoded_signal = []
    previous_sample = initial_value

    # Decode the delta modulated signal
    for bit in delta_encoded:
        if bit == 1:
            previous_sample += step_size
        else:
            previous_sample -= step_size
        decoded_signal.append(previous_sample)
    return np.array(decoded_signal)

# Parameters for the sine wave signal
frequency = 5  # Frequency of the sine wave (Hz)
sampling_rate = 1000  # Sampling rate (samples per second)
duration = 1  # Duration of the signal in seconds
step_size = 0.05  # Step size for delta modulation

# Generate the sine wave signal
t, signal = generate_sine_wave(frequency, sampling_rate, duration)

# Perform Delta Modulation
delta_encoded = delta_modulate(signal, step_size)

# Perform Delta Demodulation (reconstruction)
decoded_signal = delta_demodulate(delta_encoded, step_size)

# Plot the original signal, delta modulated signal, and decoded signal
plt.figure(figsize=(12, 8))

# Plot the original sine wave signal
plt.subplot(3, 1, 1)
plt.plot(t, signal, label='Original Signal', color='blue')
plt.title('Original Signal (Sine Wave)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot the delta modulated signal (encoded)
plt.subplot(3, 1, 2)
plt.step(t, delta_encoded, label='Delta Modulated Signal', color='red', where='post')
plt.title('Delta Modulated Signal (Encoded)')
plt.xlabel('Time [s]')
plt.ylabel('Encoded Bit (0 or 1)')
plt.grid(True)

# Plot the reconstructed signal from the delta modulation
plt.subplot(3, 1, 3)
plt.plot(t, decoded_signal, label='Decoded Signal', color='green')
plt.title('Decoded Signal from Delta Modulation')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
