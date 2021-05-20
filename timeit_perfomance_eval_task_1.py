from timeit import Timer
import matplotlib.pyplot as plt
import random
# import numpy as np
import opt_solution_task_1 as opt_solution
import simple_perfomance_eval_task_1 as other_sol


time1 = []
time2 = []

for i in range(1000):

    x = random.randint(1, 10**5+1)
    t1 = Timer("opt_solution.custom_algorithm(x)", globals=globals())
    time1.append(t1.timeit(number=100))
    t2 = Timer("other_sol.sum_using_for_loop(x)", globals=globals())
    time2.append(t2.timeit(number=100))



plt.plot(0, "b-")
plt.plot(time1, 'g^', label="custom_algorithm(x)")
plt.plot(time2, 'r^', label="sum_using_for_loop(x)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.ylabel('Running time')
plt.xlabel(f'Epoch(by epoch number in range from 1 to {"10^25"})')
plt.title('Performance of custom_algorithm(x) method for calcul sum from 1 to N')
plt.ylabel('Running time')

plt.show()