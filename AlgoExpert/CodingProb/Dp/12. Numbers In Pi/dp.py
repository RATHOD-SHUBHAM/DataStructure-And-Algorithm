# similar to pallindormic partitioning

def numbersInPi(pi, numbers):
    n = len(pi)

    cache = {x : True for x in numbers}

    dp = [0] * (n + 1)

    for i in reversed(range(n)):
        
        minSpace = float("inf")
    
        for j in range(i , n):
            curPi = pi[i : j+1]
    
            if curPi in cache:
                space = 1 + dp[j+1]
    
                minSpace = min(minSpace , space)


        dp[i] = minSpace


    return -1 if dp[0] == float("inf") else dp[0] - 1