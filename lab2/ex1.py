import numpy as np
import matplotlib.pyplot as plt

A = 2.0
f = 5.0
phi = np.pi / 4
fs = 1000.0
t = np.linspace(0, 1, int(fs), endpoint=False)

x_sin = A * np.sin(2 * np.pi * f * t + phi)
x_cos = A * np.cos(2 * np.pi * f * t + phi - np.pi / 2)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
ax1.plot(t, x_sin, color='b')
ax2.plot(t, x_cos, color='r')

plt.tight_layout()
plt.savefig('ex1.pdf', format='pdf')  
plt.show()