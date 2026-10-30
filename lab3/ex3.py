import numpy as np
import matplotlib.pyplot as plt

fs = 100
t = np.linspace(0, 1, fs, endpoint = False)
f1, f2, f3 = 3, 10, 25
x_compus = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t) + 0.3 * np.sin(2 * np.pi * f3 * t)

omega_range = np.linspace(0, 40, 200)
X_mag = [np.abs(np.sum(x_compus * np.exp(-2j * np.pi * w * t))) for w in omega_range]

fig, ax = plt.subplots(figsize = (10, 5))
ax.plot(omega_range, X_mag, color = 'crimson', linewidth = 2)
ax.grid(True)
plt.savefig("ex3.pdf")
plt.close()