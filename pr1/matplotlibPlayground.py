
import time

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)
x_fun = lambda t : 2*np.sin(t)
y_fun = lambda t : 2*np.cos(t)
x = x_fun(t)
y = y_fun(t)

plt.plot(x,y)
plt.xlabel(r'$x(t) = $', fontsize = 14)
plt.ylabel(r'$y(t)$', fontsize = 14)
plt.title(r'Parametric Curve')
plt.axis('equal')
plt.show()
time.sleep(1)

print("this is a message")