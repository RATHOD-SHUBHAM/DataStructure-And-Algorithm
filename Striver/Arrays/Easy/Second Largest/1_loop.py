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