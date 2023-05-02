# pallindrominc partition 

import math
def numbersInPi(pi, numbers):
    start_idx = 0

    min_space = recursion(start_idx, pi, numbers)

    return min_space if min_space != math.inf else -1

def recursion(idx, pi, numbers):
    # base case
    if idx == len(pi):
        return -1

    # code
    min_space = math.inf

    for i in range(idx , len(pi)):
        prefix = pi[idx : i+1]

        if prefix in numbers:
            # add a space and check
            get_space = 1 + recursion(i + 1, pi, numbers)
            print(get_space)

            min_space = min(min_space , get_space)

    return min_space