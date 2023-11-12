import math

class Solution:

    def print2largest(self,arr, n):
        largest = -1
        second_largest = -1
        
        for i in range(n):
            cur_ele = arr[i]
            
            if cur_ele > largest:
                second_largest = largest
                largest = cur_ele
            
            else:
                if cur_ele < largest and cur_ele > second_largest:
                    second_largest = cur_ele
                
        return second_largest