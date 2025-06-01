#User function Template for python3

import math
class Solution:
    def __init__(self):
        self.min_diff = math.inf
        
    def minDifference(self, arr):
        # code here
        n = len(arr)
        
        total = sum(arr)
        
        cur_sum = 0
        idx = n-1
        
        self.recursion(idx, cur_sum, total, n, arr)
        
        return self.min_diff

    def recursion(self, idx, cur_sum, total, n, arr):
        # base case
        if idx < 0:
            return
        
        arr_1 = cur_sum + arr[idx]
        arr_2 = total - arr_1
        
        cur_diff = abs(arr_1 - arr_2)
        
        self.min_diff = min(self.min_diff, cur_diff)
        
        # Logic
        take = self.recursion(idx - 1, arr_1, total, n, arr)
        
        no_take = self.recursion(idx - 1, cur_sum, total, n, arr)
        
        return


# --------------------------------- Same Solution with different approach ---------------------------------
import math
class Solution:
    def __init__(self):
        self.min_diff = math.inf
        
    def minDifference(self, arr):
        # code here
        n = len(arr)
        
        total = sum(arr)
        
        cur_sum = 0
        idx = n-1
        
        
        self.recursion(idx, cur_sum, total, n, arr)
        
        return self.min_diff

    def recursion(self, idx, cur_sum, total, n, arr):
        # base case
        if idx < 0:
            arr_1 = cur_sum
            arr_2 = total - arr_1
            
            cur_diff = abs(arr_1 - arr_2)
            
            self.min_diff = min(self.min_diff, cur_diff)
            return
        
        # Logic
        take = self.recursion(idx - 1, cur_sum + arr[idx], total, n, arr)
        
        no_take = self.recursion(idx - 1, cur_sum, total, n, arr)
        
        return
        