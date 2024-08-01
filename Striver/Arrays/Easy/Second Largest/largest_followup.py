import math

class Solution:
    def print2largest(self, arr):
        n = len(arr)
        
        first_largest = max(arr)
        second_largest =  -1
        
        for i in range(n):
            cur_ele = arr[i]
            
            if cur_ele < first_largest and cur_ele > second_largest:
                second_largest = cur_ele
        
        return second_largest