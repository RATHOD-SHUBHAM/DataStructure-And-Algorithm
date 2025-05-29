class Solution:
    def isSubsetSum (self, arr, sum):
        n = len(arr)
        
        idx = n - 1
        
        return self.recursion(idx, arr, sum)
    
    def recursion(self, idx, arr, target):
        # base case
        if idx < 0:
            return False
        
        if target == 0:
            return True
        
        # Take
        if target >= arr[idx]:
            take = self.recursion(idx - 1, arr, target - arr[idx])
        else:
            take = False
        
        
        # Dont take
        dont_take = self.recursion(idx - 1, arr, target)
        
        return take or dont_take
    


        
        