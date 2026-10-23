import numpy as np
import matplotlib.pyplot as plt

fs = 100.0
t = np.linspace(0, 1, int(fs), endpoint=False)

# subpunctul (a)
f_a = fs / 2
x_a = np.sin(2 * np.pi * f_a * t)

# subpunctul (b)
f_b = fs / 4
x_b = np.sin(2 * np.pi * f_b * t)

# subpunctul (c)
f_c = 0.0
x_c = np.sin(2 * np.pi * f_c * t)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
ax1.plot(t, x_a, 'o-')
ax2.plot(t, x_b, 'o-')
ax3.plot(t, x_c, 'o-')
plt.tight_layout()
plt.savefig('ex6.pdf', format='pdf')
plt.show()