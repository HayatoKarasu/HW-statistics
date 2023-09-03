from numpy import random as rnd
from matplotlib import pyplot as plt
import scipy.stats as stats
import numpy as np

plt.figure(figsize=(10, 10))

plt.text(0.01, 0.9, "У алмаза 57 граней. Алмаз крутится вокруг своей центральной", fontsize=15)
plt.text(0.01, 0.8, "оси. Если условно расположить грани алмаза на графике, то мы", fontsize=15)
plt.text(0.01, 0.7, "сможем увидеть, что график алмаза похож на нормальное", fontsize=15)
plt.text(0.01, 0.6, "распределение. Исходя из этого мы сможем пределить примерно", fontsize=15)
plt.text(0.01, 0.5, "математическое ожидание = 28 (на уроке сказали, что должно быть", fontsize=15)
plt.text(0.01, 0.4, "целое число). Это выпирающая грань алмаза. Она и будет", fontsize=15)
plt.text(0.01, 0.3, "подвержена наибольшему поподанию нейтронов.", fontsize=15)
plt.text(0.01, 0.2, "Наконец с помощью Пайтон мы сможем это увидеть графически", fontsize=15)
plt.text(0.01, 0.1, "и подтвердить наши ожидания, математические и личные.", fontsize=15)
plt.text(0.01, 0.01, "Математическое ожидание = 28, отклонение = 1, данных = 100000", fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.show()

data = rnd.normal(28, 1, 100000)
index = np.arange(data.shape[0])
plt.plot(index, data)
plt.show()

plt.hist(data)
plt.show()

#measurements = rnd.normal(loc = 20, scale = 5, size = 100)
stats.probplot(data, dist="norm", plot = plt)
plt.show()

#uniform_data = rnd.uniform(size=100)
#stats.probplot(uniform_data, dist="norm", plot = plt)
#plt.show()