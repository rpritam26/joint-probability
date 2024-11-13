import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Function to generate the transmitted binary signal (0s and 1s)
def generate_transmitted_signal(symbols, symbol_rate, samples_per_symbol):
    # Generate time vector for the entire duration of the signal
    t = np.linspace(0, len(symbols) / symbol_rate, len(symbols) * samples_per_symbol, endpoint=False)
    signal = np.zeros_like(t)
    # Each symbol is mapped to a pulse, and its value is placed in the corresponding time slots
    for i, symbol in enumerate(symbols):
        start_idx = i * samples_per_symbol
        end_idx = (i + 1) * samples_per_symbol
        signal[start_idx:end_idx] = symbol  # "Pulse" corresponding to the symbol
    return t, signal

# Function to apply a simple low-pass filter to simulate ISI
def apply_channel_filter(signal, cutoff_freq, symbol_rate, samples_per_symbol):
    # Create a simple low-pass filter (use a sinc filter as an approximation)
    nyquist = 0.5 * symbol_rate * samples_per_symbol  # Nyquist frequency for the given sampling rate
    cutoff = cutoff_freq / nyquist  # Normalized cutoff frequency

    # Create impulse response for a simple low-pass filter (RC or similar)
    num_samples = len(signal)
    impulse_response = np.sinc(2 * cutoff * (np.arange(-num_samples // 2, num_samples // 2)))
    impulse_response /= np.sum(impulse_response)  # Normalize the filter

    # Convolve the signal with the filter to introduce ISI
    filtered_signal = convolve(signal, impulse_response, mode='same')
    return filtered_signal

# Function to generate the eye pattern
def plot_eye_pattern(signal, samples_per_symbol, num_symbols):
    plt.figure(figsize=(10, 6))
    symbol_duration = samples_per_symbol

    # Plot each symbol period in the eye pattern
    for i in range(num_symbols - 1):
        start_idx = i * symbol_duration
        end_idx = start_idx + 2 * symbol_duration
        plt.plot(signal[start_idx:end_idx], color='blue', alpha=0.5)

    plt.title('Eye Pattern')
    plt.xlabel('Time [samples]')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

# Parameters for simulation
symbol_rate = 1000  # Symbol rate (symbols per second)
duration = 0.01  # Duration of the signal in seconds
num_symbols = 20  # Number of symbols to simulate
cutoff_freq = 0.3  # Cutoff frequency of the low-pass filter (as fraction of Nyquist)
samples_per_symbol = 100  # Samples per symbol for resolution

# Generate a random binary signal (0s and 1s)
np.random.seed(0)  # For reproducibility
symbols = np.random.choice([0, 1], size=num_symbols)

# Generate the transmitted signal (rectangular pulses for each symbol)
t, transmitted_signal = generate_transmitted_signal(symbols, symbol_rate, samples_per_symbol)

# Apply a low-pass filter to introduce ISI (simulating a real-world channel)
received_signal = apply_channel_filter(transmitted_signal, cutoff_freq, symbol_rate, samples_per_symbol)

# Plot the eye pattern of the received signal
plot_eye_pattern(received_signal, samples_per_symbol, num_symbols)
