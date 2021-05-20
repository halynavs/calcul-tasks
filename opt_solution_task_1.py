def custom_algorithm(number):
    #check if positive
    assert number > 0, "Input number must be POSITIVE"
    # check if integer
    assert isinstance(number, int), "Input number must be INTEGER"
    if number%2==1:
        return int((number+1)*(number//2)+(number+1)/2)
    else:
        return int((number + 1) * (number // 2))