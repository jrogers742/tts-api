import numpy as np
from numpy.typing import NDArray
import soundfile as sf

def generate_sin(frequency_hz: int, duration_seconds: float, sample_rate:int=22050) -> NDArray[np.float64]:
   time_axis = np.arange(sample_rate*duration_seconds)
   samples = np.sin(2 * frequency_hz * np.pi * (time_axis/sample_rate))
   return samples

print(generate_sin(frequency_hz=1, duration_seconds=1.0, sample_rate=4))

def add_sin_waves(frequency_hz_one: int, frequency_hz_two:int, duration_seconds:int, sample_rate:int=22050) -> None:
    wave_one = generate_sin(frequency_hz=frequency_hz_one, duration_seconds=duration_seconds,sample_rate=sample_rate)
    wave_two = generate_sin(frequency_hz=frequency_hz_two, duration_seconds=duration_seconds,sample_rate=sample_rate)
    new_wave = wave_one + wave_two
    normalized_wave = new_wave / 2.0
    sf.write("sine_wav.wav",normalized_wave,sample_rate)

add_sin_waves(5,10,2,44100)

def fade_in_out(audio_arr: NDArray, N: int) -> NDArray:
    audio_faded = audio_arr.copy()
    fade_in = np.linspace(0.0, 1.0, N)
    fade_out = np.linspace(1.0, 0.0, N)

    audio_faded[:N] *= fade_in
    audio_faded[-N:] *= fade_out

    return audio_faded


# Create a sample audio array
audio = np.ones(10, dtype=float)

# Apply a fade-in and fade-out over 3 samples
faded_audio = fade_in_out(audio, 3)

# Print the results
print("Original audio:", audio)
print("Faded audio:   ", faded_audio)

def compute_fft():
    pass
    