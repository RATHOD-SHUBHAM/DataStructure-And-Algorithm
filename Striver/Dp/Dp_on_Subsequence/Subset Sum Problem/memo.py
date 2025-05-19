class Solution:
    def isSubsetSum (self, arr, sum):
        n = len(arr)
        
        idx = n - 1
        
        memo = {}
        
        return self.recursion(idx, memo, arr, sum)
    
    def recursion(self, idx, memo, arr, target):
        # base case
        if idx < 0:
            return False
        
        if target == 0:
            return True
        
        if (idx, target) in memo:
            return memo[(idx, target)]
        
        # Take
        if target >= arr[idx]:
            take = self.recursion(idx - 1, memo, arr, target - arr[idx])
        else:
            take = False
        
        
        # Dont take
        dont_take = self.recursion(idx - 1, memo, arr, target)
        
        memo[(idx, target)] = take or dont_take
        
        return memo[(idx, target)]
        