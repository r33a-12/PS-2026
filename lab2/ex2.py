import numpy as np
import matplotlib.pyplot as plt

A = 1.0
f = 3.0
fs = 500.0
t = np.linspace(0, 1, int(fs), endpoint=False)

phases = [0, np.pi/4, np.pi/2, np.pi]

plt.figure(figsize=(10, 6))
for phi in phases:
    x = A * np.sin(2 * np.pi * f * t + phi)
    plt.plot(t, x)

plt.savefig('ex2_faza.pdf', format='pdf')
plt.show()

x_base = A * np.sin(2 * np.pi * f * t)
norm_x = np.linalg.norm(x_base)
snr_values = [0.1, 1, 10, 100]

plt.figure(figsize=(12, 8))
for i, snr in enumerate(snr_values):
    z = np.random.normal(0, 1, len(t))
    norm_z = np.linalg.norm(z)
    gamma = norm_x / (np.sqrt(snr) * norm_z)
    x_noisy = x_base + gamma * z
    
    plt.subplot(len(snr_values), 1, i + 1)
    plt.plot(t, x_noisy)

plt.tight_layout()
plt.savefig('ex2_zgomot.pdf', format='pdf')
plt.show()