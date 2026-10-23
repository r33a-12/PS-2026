import numpy as np
import matplotlib.pyplot as plt

fs = 1000.0
t = np.linspace(0, 1, int(fs), endpoint=False)
x = np.sin(2 * np.pi * 10 * t)

# subpunctul (a)
x_dec_a = x[::4]
t_dec_a = t[::4]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
ax1.plot(t, x)
ax1.plot(t_dec_a, x_dec_a, 'ro-')

# subpunctul (b)
x_dec_b = x[1::4]
t_dec_b = t[1::4]

ax2.plot(t, x)
ax2.plot(t_dec_b, x_dec_b, 'go-')

plt.tight_layout()
plt.savefig('ex7.pdf', format='pdf')
plt.show()