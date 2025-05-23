#User function Template for python3
class Solution:
    def perfectSum(self, arr, target):
        # code here
        n = len(arr)
        memo = {}
        
        def recursion(idx, cur_sum):
            if idx < 0:
                if cur_sum == target:
                    return 1
                else:
                    return 0
                    
            if (idx, cur_sum) in memo:
                return memo[(idx, cur_sum)]
            
            take = recursion(idx - 1, cur_sum + arr[idx])
            no_take = recursion(idx - 1, cur_sum)
            
            memo[(idx, cur_sum)] = take + no_take
            
            return memo[(idx, cur_sum)]
            
        idx = n - 1
        cur_sum = 0
        
        return recursion(idx, cur_sum)
    
# --------------------------- Same Solution with different approach ---------------------------

#User function Template for python3
class Solution:
    def perfectSum(self, arr, target):
        # code he
        n = len(arr)
        
        idx = n - 1
        
        memo = {}
        
        return self.recursion(idx, memo, n, arr, target)

    def recursion(self, idx, memo, n, arr, target):
        # base case
        if idx < 0:
            if target == 0:
                return 1
            else:
                return 0
                
        if (idx, target) in memo:
            return memo[(idx, target)]
                
        # Logic
        if target >= arr[idx]:
            take = self.recursion(idx - 1, memo, n, arr, target - arr[idx])
        else:
            take = 0
            
        no_take = self.recursion(idx - 1, memo, n, arr, target)
        
        memo[(idx, target)] = take + no_take
        
        return memo[(idx, target)]
