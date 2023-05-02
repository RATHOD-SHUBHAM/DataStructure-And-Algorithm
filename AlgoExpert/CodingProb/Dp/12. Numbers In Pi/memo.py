import math
def numbersInPi(pi, numbers):
    number = {x : True for x in numbers}
    
    start_idx = 0

    memo = [None] * len(pi)
    
    memo[start_idx] = recursion(start_idx, memo, pi, number)

    return memo[start_idx] if memo[start_idx] != math.inf else -1

def recursion(idx, memo, pi, number):
    # base case
    if idx == len(pi):
        return -1

    if memo[idx]:
        return memo[idx]

    # code
    min_space = math.inf

    for i in range(idx , len(pi)):
        # grab the values in numbers
        prefix = pi[idx : i+1]

        if prefix in number:
            # add a space and check
            get_space = 1 + recursion(i + 1, memo, pi, number)
            print(get_space)

            min_space = min(min_space , get_space)

    memo[idx] = min_space
    return memo[idx]
            