# Tc = O( n * denoms) | Sc: O( n )

# in 2D dp - we are looking at one row above and newTarget value
def numberOfWaysToMakeChange(n, denoms):
    dp = [0 for _ in range(n+1) ]
    dp[0] = 1

    for coinIdx in range(len(denoms)):
        for curAmount in range(1, n + 1):
            # check if i can use the coin
            if curAmount >= denoms[coinIdx]:
                # we dont look up : we just preserve it
                newAmount = curAmount - denoms[coinIdx]
                dp[curAmount] += dp[newAmount]

    return dp[-1]