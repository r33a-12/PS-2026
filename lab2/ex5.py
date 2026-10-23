import numpy as np
import sounddevice as sd

fs = 44100
t1 = np.linspace(0, 0.5, int(fs * 0.5), endpoint=False)
t2 = np.linspace(0, 0.5, int(fs * 0.5), endpoint=False)

x1 = np.sin(2 * np.pi * 300 * t1)
x2 = np.sin(2 * np.pi * 800 * t2)

x_concat = np.concatenate((x1, x2))

sd.play(x_concat, fs)
sd.wait()