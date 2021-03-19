import matplotlib.pyplot as plt
import numpy as np
from random import randint
i = 1

diffs = []

while i <= 1e4:
    r1 = np.random.normal(0,1)
    r2 = np.random.normal(0,1)
    r3 = np.random.normal(0,1)

    diff = np.sqrt((r1 - r2) * (r1 - r2) + 4 * r3 ** 2)
    diffs.append(diff)
    i +=1

norm_diffs = diffs / np.mean(diffs)

n, bins, patches = plt.hist(norm_diffs, 250, density = True, stacked = True, facecolor='black', alpha=0.5)
# Die Vergleichslinie
x = np.arange(0,5,0.1)
y =(np.pi/2) * x * np.exp(-(np.pi*(x**2))/4)
plt.plot(x, y, linewidth = 2)

plt.axis([0, 3.5, 0, 1])
plt.grid(True)
plt.show()
