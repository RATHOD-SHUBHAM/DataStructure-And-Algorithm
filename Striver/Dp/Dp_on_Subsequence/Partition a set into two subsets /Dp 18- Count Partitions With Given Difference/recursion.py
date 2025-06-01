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




def countPartitions(n: int, d: int, arr: List[int]) -> int:
    # write your code here
    total = sum(arr)

    # base case
    """
    Edge Cases:
    1. (S + D) must be even - otherwise no valid partition exists
    2. D < S difference can't be larger than total sum
    """
    if d > total or (total + d) % 2 != 0:
        return 0
    
    target = (d + total) // 2

    idx = n - 1

    MOD = (10 ** 9) + 7

    return recursion(idx, target, arr) % MOD


