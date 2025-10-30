# --------- 2 Loops ----------------------
import math

class Solution:
    def print2largest(self,arr, n):

        largest = -1
        second_largest = -1

        for i in range(n):
            cur_ele = arr[i]
            
            if cur_ele > largest:
                largest = cur_ele

        for i in range(n):
            cur_ele = arr[i]
            
            if cur_ele < largest and cur_ele > second_largest:
                second_largest = cur_ele
                
        return second_largest

# --------- 1 Loop ----------------------
class Solution:
    def print2largest(self,arr, n):
        # code here
        largest = arr[0]
        second_largest = -1
        
        for i in range(n):
            num = arr[i]
            
            if num > largest:
                second_largest = largest
                largest = num
                continue
            
            if num > second_largest and num < largest:
                second_largest = num
        
        return second_largest

# --------- Same Solution Different Way ----------------------  
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n = len(arr)
        
        largest = arr[0]
        second = -1
        
        for i in range(1, n):
            if arr[i] > largest:
                second = largest
                largest = arr[i]
            elif arr[i] < largest and arr[i] > second:
                second = arr[i]
        
        return second
    
# --------- Follow up to Largest Element ----------------------

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