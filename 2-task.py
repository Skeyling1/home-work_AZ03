#2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.

import matplotlib.pyplot as plt
import numpy as np

random_array_a = np.random.rand(500)
random_array_b = np.random.rand(500)

plt.scatter(random_array_a, random_array_b)
plt.xlabel("ось X")
plt.ylabel("ось Y")
plt.title("Диаграмма рассеяния для двух наборов случайных данных")
plt.grid(True)
plt.show()