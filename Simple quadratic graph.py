import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 24)
y = x**2

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
