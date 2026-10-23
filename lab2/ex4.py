import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth

fs = 1000.0
t = np.linspace(0, 1, int(fs), endpoint=False)

x1 = np.sin(2 * np.pi * 5 * t)
x2 = sawtooth(2 * np.pi * 5 * t)
x_sum = x1 + x2

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
ax1.plot(t, x1)
ax2.plot(t, x2)
ax3.plot(t, x_sum)
plt.tight_layout()
plt.savefig('ex4.pdf', format='pdf')
plt.show()