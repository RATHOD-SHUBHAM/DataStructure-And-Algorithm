from typing import List

def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    n = len(arr)

    idx = n - 1

    cur_sum = 0

    return recursion(idx, cur_sum, arr, k)

def recursion(idx: int, cur_sum: int, arr: List[int], k: int) -> int:
    # base case
    if idx < 0:
        if cur_sum == k:
            return 1
        else:
            return 0
        
    # Logic
    if arr[idx] <= k:
        take = recursion(idx - 1, cur_sum + arr[idx], arr, k)
    else:
        take = 0

    notTake = recursion(idx - 1, cur_sum, arr, k)
    
    return take + notTake


# ----------------------------------- Memoization -----------------------------------
from typing import List

def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    n = len(arr)

    idx = n - 1

    cur_sum = 0

    memo = {}

    return recursion(idx, cur_sum, memo, arr, k)

def recursion(idx: int, cur_sum: int, memo:dict ,arr: List[int], k: int) -> int:
    # base case
    if idx < 0:
        if cur_sum == k:
            return 1
        else:
            return 0
        
    if (idx, cur_sum) in memo:
        return memo[(idx, cur_sum)]
        
    # Logic
    if arr[idx] <= k:
        take = recursion(idx - 1, cur_sum + arr[idx], memo, arr, k)
    else:
        take = 0

    notTake = recursion(idx - 1, cur_sum, memo, arr, k)
    
    memo[(idx, cur_sum)] = take + notTake

    return memo[(idx, cur_sum)]

# ------------------------------------- Tabulation -----------------------------------

from typing import List

def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    n = len(arr)

    dp = [[0 for _ in range(k+1)]for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1

    if arr[0] == 0:
        dp[0][0] = 2
    elif arr[0] <= k:
        dp[0][arr[0]] = 1

    for idx in range(1, n):
        for cur_sum in range(k+1):
            if arr[idx] <= cur_sum:
                take = dp[idx-1][cur_sum - arr[idx]]
            else:
                take = 0

            notTake = dp[idx-1][cur_sum]
            
            dp[idx][cur_sum] = take + notTake
    
    return dp[n-1][k] % ( (10 ** 9) + 7)

# ------------------------------------- Space Optimization -----------------------------------

from typing import List

def findWays(arr: List[int], k: int) -> int:
    n = len(arr)

    MOD = (10 ** 9) + 7

    dp = [0 for _ in range(k+1)]

    if arr[0] == 0:
        dp[0] = 2
    else:
        dp[0] = 1
        if arr[0] <= k:
            dp[arr[0]] = 1
    
    for idx in range(1, n):
        temp = [0 for _ in range(k+1)]

        for cur_sum in range(k+1):
            if arr[idx] <= cur_sum:
                take = dp[cur_sum - arr[idx]]
            else:
                take = 0
            
            no_take = dp[cur_sum]

            temp[cur_sum] = take + no_take

        dp = temp
    
    return dp[k] % MOD
