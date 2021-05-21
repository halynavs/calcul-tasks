from timeit import Timer
import matplotlib.pyplot as plt
import numpy as np

time1 = []

for i in range(1000):
    matrix = np.random.randint(2, size=(10**2,10**2))
    t1 = Timer("np.sum(matrix)", globals=globals())
    time1.append(t1.timeit(number=1000))

plt.plot(0, "b-")
plt.plot(time1, 'g^', label="np.sum(matrix)")

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.ylabel('Running time')
plt.xlabel(f'Epoch')
plt.title('Performance of np.sum(matrix) method')
plt.ylabel('Running time')

plt.show()