#1. Создай гистограмму для случайных данных, сгенерированных с помощью функции `numpy.random.normal`.

import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0 # Среднее значение
std_dev = 1 # Стандартное отклонение
num_samples = 1000 # Количество образцов
# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)


plt.hist(data, bins = 100)
plt.title("Гистограмма для случайных данных")
plt.xlabel("случайные величины")
plt.ylabel("частота")
plt.show()