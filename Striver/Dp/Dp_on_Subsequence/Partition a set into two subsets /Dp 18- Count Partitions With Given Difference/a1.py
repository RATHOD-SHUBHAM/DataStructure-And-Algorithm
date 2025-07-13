from os import *
from sys import *
from collections import *
from math import *

from typing import List


def recursion(idx, target, arr):
    # base case
    if idx < 0:
        if target == 0:
            return 1
        else:
            return 0
        
    # Logic
    if arr[idx] <= target:
        take = recursion(idx - 1, target - arr[idx], arr)
    else:
        take = 0
    
    no_take = recursion(idx - 1, target, arr)

    return take + no_take


"""

    Count partitions where S1 >= S2 and S1 - S2 = d
    
    Mathematical Analysis:
    - Let S1 = sum of subset 1, S2 = sum of subset 2
    - We know: S1 + S2 = total (sum of all elements)
    - We want: S1 - S2 = d
    
    Solving these equations:
    - From S1 + S2 = total and S1 - S2 = d
    - Adding: 2*S1 = total + d, so S1 = (total + d) / 2
    - Subtracting: 2*S2 = total - d, so S2 = (total - d) / 2
    
    For valid partitions:
    1. S1 and S2 must be integers, so (total + d) must be even
    2. S1 >= 0 and S2 >= 0, so total >= d
    3. S1 <= total (subset sum can't exceed total)



"""

def countPartitions(n: int, d: int, arr: List[int]) -> int:
    # write your code here
    total = sum(arr)

    # base case
    """
    Edge Cases:
    1. (S + D) must be even - otherwise no valid partition exists
    2. D < S difference can't be larger than total sum
    """
    """
    Mathematical constraint:

    We need S1 = (total + d) / 2
    For S1 to be an integer, (total + d) must be even
    
    """
    if d > total or (total + d) % 2 != 0:
        return 0
    
    target = (d + total) // 2

    idx = n - 1

    MOD = (10 ** 9) + 7

    return recursion(idx, target, arr) % MOD


# ------------------------ Memoization ------------------------
from os import *
from sys import *
from collections import *
from math import *

from typing import List


def recursion(idx, memo, target, arr):
    # base case
    if idx < 0:
        if target == 0:
            return 1
        else:
            return 0
    
    if (idx, target) in memo:
        return memo[(idx, target)]
        
    # Logic
    if arr[idx] <= target:
        take = recursion(idx - 1, memo, target - arr[idx], arr)
    else:
        take = 0
    
    no_take = recursion(idx - 1, memo, target, arr)

    memo[(idx, target)] = take + no_take

    return memo[(idx, target)]




def countPartitions(n: int, d: int, arr: List[int]) -> int:
    # write your code here
    total = sum(arr)

    # base case
    if d > total or (total + d) % 2 != 0:
        return 0
    
    target = (d + total) // 2

    idx = n - 1

    MOD = (10 ** 9) + 7

    memo = {}

    return recursion(idx, memo, target, arr) % MOD


# ------------------------ Tabulation ------------------------

from os import *
from sys import *
from collections import *
from math import *

from typing import List


def countPartitions(n: int, d: int, arr: List[int]) -> int:
    # write your code here
    total_sum = sum(arr)

    """
    Edge Cases:
    1. (S + D) must be even - otherwise no valid partition exists
    2. D < S difference can't be larger than total sum
    """

    if (total_sum + d) % 2 != 0 or (d > total_sum):
        return 0
    
    """
    If we consider s2 to be our target
    if (total_sum - d) % 2 != 0 or (total_sum - d < 0):
        return 0
    """

    target = (total_sum + d) // 2
    

    return findWays(arr, target)

def findWays(arr, target):
    n = len(arr)

    dp = [[0 for _ in range(target + 1)]for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1
    

    if arr[0] == 0:
        dp[0][0] = 2
    else:
        if arr[0] <= target:
            dp[0][arr[0]] = 1
    
    for idx in range(1, n):
        for cur_sum in range(target + 1):
            if cur_sum >= arr[idx]:
                take = dp[idx-1][cur_sum - arr[idx]]
            else:
                take = 0
            
            no_take = dp[idx-1][cur_sum]
        
            dp[idx][cur_sum] = take + no_take
    
    return dp[n-1][target] % ((10 ** 9) + 7)


# ------------------------ Space Optimized ------------------------
from os import *
from sys import *
from collections import *
from math import *

from typing import List


def countPartitions(n: int, d: int, arr: List[int]) -> int:
    # write your code here
    total_sum = sum(arr)

    """
    Edge Cases:
    1. (S + D) must be even - otherwise no valid partition exists
    2. D < S difference can't be larger than total sum
    """

    if (total_sum + d) % 2 != 0 or (d > total_sum):
        return 0
    
    """
    If we consider s2 to be our target
    if (total_sum - d) % 2 != 0 or (total_sum - d < 0):
        return 0
    """

    target = (total_sum + d) // 2
    

    return findWays(arr, target)

def findWays(arr, target):
    n = len(arr)

    dp = [0 for _ in range(target + 1)]

    dp[0] = 1
    

    if arr[0] == 0:
        dp[0] = 2
    else:
        if arr[0] <= target:
            dp[arr[0]] = 1
    
    for idx in range(1, n):
        temp = [0 for _ in range(target + 1)]
        for cur_sum in range(target + 1):
            if cur_sum >= arr[idx]:
                take = dp[cur_sum - arr[idx]]
            else:
                take = 0
            
            no_take = dp[cur_sum]
        
            temp[cur_sum] = take + no_take
        
        dp = temp
    
    return dp[target] % ((10 ** 9) + 7)