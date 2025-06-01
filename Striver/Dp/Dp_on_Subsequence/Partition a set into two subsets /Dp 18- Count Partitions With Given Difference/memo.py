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


