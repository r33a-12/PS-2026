import numpy as np
import matplotlib.pyplot as plt

fs = 200
t = np.linspace(0, 1, fs, endpoint=False)
f_signal = 5
x = np.sin(2 * np.pi * f_signal * t)
omegas = [1, 5, 15, 30]
theta = np.linspace(0, 2 * np.pi, 200)

fig, ax = plt.subplots(figsize = (6, 6))
z_match = x * np.exp(-2j * np.pi * f_signal * t)

ax.plot(np.real(z_match), np.imag(z_match), color='purple', alpha=0.6)
ax.scatter(np.real(z_match), np.imag(z_match), c=np.arange(len(t)), cmap='viridis', s=30)
ax.plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.3)
ax.grid(True)

plt.savefig("ex2_fig1.pdf")
plt.close()

fig, axes = plt.subplots(2, 2, figsize = (10, 10))
axes = axes.flatten()
for idx, w in enumerate(omegas):
    z_w = x * np.exp(-2j * np.pi * w * t)
    axes[idx].plot(np.real(z_w), np.imag(z_w), color='teal', alpha = 0.6)
    axes[idx].scatter(np.real(z_w), np.imag(z_w), c=np.arange(len(t)), cmap='plasma', s=20)
    axes[idx].plot(np.cos(theta), np.sin(theta), 'k--', alpha = 0.3)
    axes[idx].grid(True)
    axes[idx].set_title(f"omega = {w} hz")

plt.tight_layout()
plt.savefig("ex2_fig2.pdf")
plt.close()