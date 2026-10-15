import numpy as np
import matplotlib.pyplot as plt

# subpunctul (a)
f = 400
n = 1600
d = 0.02

t = np.linspace(0, d, n)
x = np.sin(2 * np.pi * f * t)

plt.figure(figsize = (10, 4))
plt.plot(t, x)
plt.title('semnal sinusoidal 400hz')
plt.grid(True)
plt.savefig('ex2-a.pdf', format='pdf')  
plt.show()

# subpunctul (b)
f = 800
d = 3
n = 8000

t = np.arange(0, d, 1/n)
x = np.sin(2 * np.pi * f * t)

plt.figure(figsize = (10, 4))
plt.plot(t, x)
plt.title('semnal sinusoidal 800hz')
plt.grid(True)
plt.savefig('ex2-b.pdf', format='pdf')
plt.show()

# subpunctul (c)
f = 240

t = np.arange(0, 0.02, 1/20000)
x = 2 * (np.mod(f * t, 1)) - 1

plt.figure(figsize = (10, 4))
plt.plot(t, x)
plt.title('semnal sawtooth 240hz')
plt.grid(True)
plt.savefig('ex2-c.pdf', format='pdf')
plt.show()

# subpunctul (d)
f = 300

t = np.arange(0, 0.02, 1/20000)
x = np.sign(np.sin(2 * np.pi * f * t))

plt.figure(figsize = (10, 4))
plt.plot(t, x)
plt.title('semnal square 300hz')
plt.grid(True)
plt.savefig('ex2-d.pdf', format='pdf')
plt.show()

# subpunctul (e)
i_rand = np.random.rand(128, 128)

plt.figure(figsize=(6, 6))
plt.imshow(i_rand, cmap='gray')
plt.title('semnal 2D aleator')
plt.savefig('ex2-e.pdf', format='pdf')
plt.show()

# subpunctul (f)
i_cust = np.zeros((128, 128))
i_cust[32:96, 32:96] = 1

plt.figure(figsize=(6, 6))
plt.imshow(i_cust, cmap='gray')
plt.title('semnal 2D custom (idk patrat alb in patrat negru)')
plt.savefig('ex2-f.pdf', format='pdf')
plt.show()
