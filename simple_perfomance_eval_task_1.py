import time

number = 10**7
time0 = time.time()

# using FOR loop
def sum_using_for_loop(number):
    #check if positive
    assert number > 0, "Input number must be POSITIVE"
    # check if integer
    assert isinstance(number, int), "Input number must be INTEGER"

    sum = 0
    for i in range(number+1):
        sum +=i
    return sum

print(f"---Sum from 1 to 10^7 = {sum_using_for_loop(number)} by"+'\033[1m'+ "  by sum_using_for_loop()"+ '\033[0m')
print("    Executing time of sum_using_for_loop(10^7): %s seconds" % (time.time() - time0))



# using sum func
time1 = time.time()
def sum_using_sum_func(number):

    # check if positive
    assert number > 0, "Input number must be POSITIVE"
    # check if integer
    assert isinstance(number, int), "Input number must be INTEGER"
    return sum(range(number+1))

print(f"---Sum from 1 to 10^7 = {sum_using_sum_func(number)} by"+'\033[1m'+ " sum_using_sum_func()"+ '\033[0m')
print("    Executing time of sum_using_sum_func(10^7): %s seconds" % (time.time() - time1))

time4 = time.time()

# simple custom func
def custom_algorithm(number):
    #check if positive
    assert number > 0, "Input number must be POSITIVE"
    # check if integer
    assert isinstance(number, int), "Input number must be INTEGER"
    if number%2==1:
        return int((number+1)*(number//2)+(number+1)/2)
    else:
        return int((number + 1) * (number // 2))


print(f"---Sum from 1 to 10^7 = {custom_algorithm(10**25)} by"+'\033[1m'+ " custom_algorithm()"+ '\033[0m')
print("    Executing time of custom_algorithm(10^7): %s seconds" % (time.time() - time4))

