class Solution:
    def isBSTTraversal(self, arr):
        n = len(arr)
        
        # Array has one or no element
        if n == 0 or n == 1:
            return True
    
        for i in range(1, n):
            # Unsorted pair found
            if arr[i-1] >= arr[i]: # assumed that there are no duplicate
                return False
    
        # No unsorted pair found
        return True