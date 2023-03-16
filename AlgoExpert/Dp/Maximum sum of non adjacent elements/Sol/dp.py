# https://leetcode.com/problems/house-robber/discuss/1753812/Maximum-Sum-of-Non-Adjacent-Elements-or-O(1)

# Tc and Sc : O(n)
# Brute Force
def maxSubsetSumNoAdjacent(array):
    # base case
    if len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    # code
    n = len(array)

    # store all the max value up until current idx i
    dp = [None] * n
    dp[0] = array[0]
    dp[1] = max(array[0], array[1])

    for i in range(2, n):
        # max value till adjacent node , or max value + curr val of non adj node
        take = array[i] + dp[i-2]
        dontTake = 0 + dp[i-1]
        dp[i] = max(take, dontTake)

    return dp[-1]
	
	