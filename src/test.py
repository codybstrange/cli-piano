import numpy as np
from scipy.io.wavfile import write

# Sampling parameters
sample_rate = 44100  # Samples per second
duration = 2.0  # seconds
frequency = 261.63  # Middle C frequency in Hz

# Generate the time values
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate the sine wave
waveform = 0.15 * np.sin(2 * np.pi * frequency * t)  # Amplitude scaled to 0.5

# Convert to 16-bit PCM format
waveform_int16 = np.int16(waveform * 32767)

# Save as a WAV file
write("middle_C.wav", sample_rate, waveform_int16)

print("Audio file 'middle_C.wav' created!")

