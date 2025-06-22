import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(500) * 10  # 500 numbers between 0-10
y = np.random.rand(500) * 100 # 500 numbers between 0-100

plt.scatter(x,y,
            alpha=0.4,
            s=45,
            marker="x"  # x or o
            )

plt.show()