# Tc: O(n^2 + m) | Sc: O(m + n)
import math
def numbersInPi(pi, numbers):
    number = {x : True for x in numbers}
    
    n = len(pi)

    dp = [math.inf] * (n + 1)
    dp[-1] = -1
    
    for i in reversed(range(n)):
        for j in range(i, n):
            # grab the values in numbers
            prefix = pi[i : j+1]

            # check if this value is present
            if prefix in number:
                # get the number of space from the next value
                get_space = 1 + dp[j + 1]
    
                dp[i] = min(dp[i] , get_space)

    return dp[0] if dp[0] != math.inf else -1