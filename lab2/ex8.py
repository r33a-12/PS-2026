import numpy as np
import matplotlib.pyplot as plt

alpha = np.linspace(-np.pi / 2, np.pi / 2, 1000)
sin_alpha = np.sin(alpha)
taylor = alpha
pade = (alpha - (7 * alpha**3) / 60) / (1 + (alpha**2) / 20)

error_taylor = np.abs(sin_alpha - taylor)
error_pade = np.abs(sin_alpha - pade)

plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(alpha, sin_alpha, color='black')
plt.plot(alpha, taylor, linestyle='--')
plt.plot(alpha, pade, linestyle=':')

plt.subplot(2, 1, 2)
plt.plot(alpha, error_taylor)
plt.plot(alpha, error_pade)
plt.yscale('log')

plt.tight_layout()
plt.savefig('ex8.pdf', format='pdf')
plt.show()