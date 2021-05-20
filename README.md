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

 
        
