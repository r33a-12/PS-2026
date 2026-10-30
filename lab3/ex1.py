import numpy as np
import matplotlib.pyplot as plt

N = 8
n = np.arange(N).reshape((N, 1))
k = np.arange(N).reshape((1, N))
F = np.exp(-2j * np.pi * n * k / N)

fig, axes = plt.subplots(N, 2, figsize = (10, 2 * N))
for i in range(N):
    axes[i, 0].plot(np.real(F[i, :]), 'o-', color = 'blue')
    axes[i, 0].grid(True)
    axes[i, 1].plot(np.imag(F[i, :]), 'o-', color = 'orange')
    axes[i, 1].grid(True)

plt.tight_layout()
plt.savefig("ex1.pdf")
plt.close()

FH_F = np.conj(F).T @ F
is_unitary = np.allclose(FH_F, N * np.eye(N))
norm_val = np.linalg.norm(FH_F - N * np.eye(N))