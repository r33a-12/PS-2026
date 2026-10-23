import numpy as np
import sounddevice as sd
from scipy.io import wavfile

fs = 44100
t = np.linspace(0, 1, fs, endpoint=False)
x = np.sin(2 * np.pi * 440 * t)

sd.play(x, fs)
sd.wait()

wavfile.write('semnal.wav', fs, x)
rate, loaded_x = wavfile.read('semnal.wav')