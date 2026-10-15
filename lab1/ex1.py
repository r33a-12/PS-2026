import numpy as np
import matplotlib.pyplot as plt

# subpunctul (a)
t = np.arange(0, 0.03, 0.0005)

# subpunctul (b)
x = np.cos(520 * np.pi * t + np.pi / 3)
y = np.cos(280 * np.pi * t - np.pi / 3)
z = np.cos(120 * np.pi * t + np.pi / 3)

fig, axs = plt.subplots(3, 1, figsize=(10, 8))

axs[0].plot(t, x)
axs[0].set_title('x(t) = cos(520*pi*t + pi/3)')
axs[0].grid(True)

axs[1].plot(t, y)
axs[1].set_title('y(t) = cos(280*pi*t - pi/3)')
axs[1].grid(True)

axs[2].plot(t, z)
axs[2].set_title('z(t) = cos(120*pi*t + pi/3)')  
axs[2].grid(True)

xmin = 0
xmax = 0.03

for ax in axs.flat:
    ax.set_xlim([xmin, xmax])
    
plt.tight_layout()
plt.savefig('ex1-b.pdf', format='pdf')  
plt.show()

# subpunctul (c)
s = np.arange(0, 0.0301, 1/200)

xs = np.cos(520 * np.pi * s + np.pi / 3)
ys = np.cos(280 * np.pi * s - np.pi / 3)
zs = np.cos(120 * np.pi * s + np.pi / 3)

fig, axs = plt.subplots(3, 1, figsize=(10, 8))

axs[0].stem(s, xs)
axs[0].plot(t, x)
axs[0].set_title('x[n] eșantionat și x(t) continuu')
axs[0].set_ylabel('amplitudine')
axs[0].grid(True)

axs[1].stem(s, ys)
axs[1].plot(t, y)
axs[1].set_title('y[n] eșantionat și y(t) continuu')
axs[1].set_ylabel('amplitudine')
axs[1].grid(True)

axs[2].stem(s, zs)
axs[2].plot(t, z)
axs[2].set_title('z[n] eșantionat și z(t) continuu')
axs[2].set_ylabel('amplitudine')
axs[2].grid(True)

for ax in axs.flat:
    ax.set_xlim([xmin, xmax])
    
plt.tight_layout()
plt.savefig('ex1-c.pdf', format='pdf')  
plt.show()