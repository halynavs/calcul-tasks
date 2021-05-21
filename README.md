# calcul-tasks
## Task 1.
#### You have a positive integer number N as an input. Please write a program in Python 3 that calculates the sum in range 1 and N.

Limitations:
N <= 10^25;
Execution time: 0.1 seconds.

Examples:

Input: 1
Output: 1

Input: 3
Output: 6

Input 10:
Output: 55

### Solution 
As we deal only with input number(N), we can think about set(1toN), which sum we need to calculate, as sorted set of numbers 
[opt_solution_task_1.py](https://github.com/halynavs/calcul-tasks/blob/main/opt_solution_task_1.py)

```
def custom_algorithm(number):

    #check if positive
    assert number > 0, "Input number must be POSITIVE"
    
    # check if integer
    assert isinstance(number, int), "Input number must be INTEGER"
    
    if number%2==1:
        return int((number+1)*(number//2)+(number+1)/2)
    else:
        return int((number + 1) * (number // 2))
 ```
        
        
### Result
![Result](https://github.com/halynavs/calcul-tasks/blob/main/images/results.png)
 
### Performance evaluation
Comparisson with function with for loop and with build in sum()

[simple_perfomance_eval_task_1.py](https://github.com/halynavs/calcul-tasks/blob/main/simple_perfomance_eval_task_1.py)

![simple_perfomance_eval](https://github.com/halynavs/calcul-tasks/blob/main/images/simple_perfomance_eval.png)

[timeit_perfomance_eval_task_1.py](https://github.com/halynavs/calcul-tasks/blob/main/timeit_perfomance_eval_task_1.py)

![timeit_perfomance_eval](https://github.com/halynavs/calcul-tasks/blob/main/images/timeit_perfomance_eval.png)



### Conclussion
custom_algorithm() looks stable(green line) and way faster

Executing time on 10^25 = 0.0 seconds


## Task 2.
#### You have a matrix MxN that represents a map. There are 2 possible states on the map: 1 - islands, 0 - ocean. Your task is to calculate the number of islands in the most effective way. Please write code in Python 3.

Examples:
Input:

3 3

0 1 0

0 0 0

0 1 1

Output: 3

Input:

3 4 

0 0 0 1

0 0 1 0

0 1 0 0

Output: 3

Input:

3 4

0 0 0 1

0 0 1 1

0 1 0 1

Output: 5

### Solution 
As we deal with binary matrix and the task is calculate sum of ones, the most effective way, in my opinion, is sum all elements in matrix. 
[solution_task_2.py](https://github.com/halynavs/calcul-tasks/blob/main/solution_task_2.py)

```
def islands_count(matrix):
    print(np.sum(matrix))
 ```
        
        
### Result
![Result](https://github.com/halynavs/calcul-tasks/blob/main/images/result2.png)
[tests_task_2.py](https://github.com/halynavs/calcul-tasks/blob/main/tests_task_2.py)
 
### Performance evaluation
using timeit(1000 times with random matrix size=(10^2,10^2))
```
for i in range(1000):
    matrix = np.random.randint(2, size=(10**2,10**2))
    t1 = Timer("np.sum(matrix)", globals=globals())
    time1.append(t1.timeit(number=1000))
    
```

[timeit_perfomance_eval_task_2.py](https://github.com/halynavs/calcul-tasks/blob/main/timeit_perfomance_eval_task_2.py)

![timeit_perfomance_eval2](https://github.com/halynavs/calcul-tasks/blob/main/images/timeit_perfomance_eval2.png)



### Conclussion
islands_count() looks stable(green line) 



 
        
