# -------------------- BaackTraack --------------------------

# Tc and Sc: O(Exponential)

def numberOfWaysToMakeChange(n, denoms):
    curTarget = 0
    curIdx = 0

    total_no_of_ways = [0]

    backTrack(curIdx , curTarget, n, denoms, total_no_of_ways)
    return total_no_of_ways[0]

def backTrack(curIdx , curTarget, n, denoms, total_no_of_ways):
    # base case
    if curTarget == n:
        total_no_of_ways[0] += 1
        return 
    if curTarget > n or curIdx >= len(denoms):
        return

    # incldue the current coin
    newTarget = curTarget + denoms[curIdx]
    backTrack(curIdx , newTarget, n, denoms, total_no_of_ways)

    # do not include the current coin 
    # target will remain same - but idx should move
    backTrack(curIdx + 1, curTarget, n, denoms, total_no_of_ways)

    return 

# -------------------- End Of backTrack -----------------------------


# -------------------- Recursive -----------------------------

# Tc and Sc: O(Exponential)

def numberOfWaysToMakeChange(n, denoms):
    curTarget = 0
    curIdx = 0

    return recursive(curIdx , curTarget, n, denoms)
    

def recursive(curIdx , curTarget, n, denoms):
    # base case
    if curTarget == n:
        return 1
    
    if curTarget > n or curIdx >= len(denoms):
        return 0

    # incldue the current coin
    newTarget = curTarget + denoms[curIdx]

    # no_of_ways = f(include the current value) + f(without including the current value)

    return recursive(curIdx , newTarget, n, denoms) + recursive(curIdx + 1 , curTarget, n, denoms)



# -------------------- End Of Recursive -----------------------------

# -------------------- Memoization -----------------------------

# Tc = O( n * denoms) | Sc: O( n * denoms) + O(n)
def numberOfWaysToMakeChange(n, denoms):
    curTarget = 0
    curIdx = 0

    memo = [[None for _ in range(n+1)] for _ in range(len(denoms) + 1)]

    return memoization(curIdx , curTarget, memo, n, denoms)
    

def memoization(curIdx , curTarget, memo, n, denoms):
    # base case    
    if curTarget == n:
        return 1
    
    if curTarget > n or curIdx >= len(denoms):
        return 0

    if memo[curIdx][curTarget] != None:
        return memo[curIdx][curTarget]

    # Target logic
    # incldue the current coin
    newTarget = curTarget + denoms[curIdx]

    # include the current coin + dont include the current coin
    memo[curIdx][curTarget] = memoization(curIdx , newTarget, memo, n, denoms) + memoization(curIdx + 1 , curTarget, memo, n, denoms)
   
    return memo[curIdx][curTarget]


# -------------------- End of memoization -----------------------------

# -------------------- 2D Dp -----------------------------

# Tc = O( n * denoms) | Sc: O( n * denoms)
def numberOfWaysToMakeChange(n, denoms):
    curTarget = 0
    curIdx = 0

    dp = [[0 for _ in range(n+1)] for _ in range(len(denoms) + 1)]

    # when i have no coins - I can make no amount
    # so 0th row will be all zero
    for col in range(n  + 1):
        dp[0][col] = 0

    # when i have some coin , in how many way can i make amount 0
    # 1 way - by not using the coins. i can make spend amount 0
    # so 0th col will be 1
    for row in range(len(denoms) + 1):
        dp[row][0] = 1

    # starting from row 1 and col 1
    for coinIdx in range(1, len(denoms) + 1):
        for curAmount in range(1, n + 1):
            # check if i can use the current coin
            # if i had 5 rupee coin but i have to 2 rupee out of it - is it possible
            if curAmount >= denoms[coinIdx - 1]:
                # use the coin + dont use the coin
                newAmount = curAmount - denoms[coinIdx - 1] # get the no of ways to reach new amount if i use the current coin
                dp[coinIdx][curAmount] = dp[coinIdx][newAmount] + dp[coinIdx - 1][curAmount]
            else:
                dp[coinIdx][curAmount] = dp[coinIdx - 1][curAmount]

    return dp[-1][-1]

# -------------------- End of 2D Dp -----------------------------

# -------------------- 1D Dp -----------------------------

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

# -------------------- End of 1D Dp -----------------------------