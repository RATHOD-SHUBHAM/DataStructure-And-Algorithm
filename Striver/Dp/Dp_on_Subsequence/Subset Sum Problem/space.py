class Solution:
    def isSubsetSum (self, arr, sum):
        # code here
        n = len(arr)
        
        dp = [False for _ in range(sum+1)]
        
        # Base case: empty subset can form sum = 0
        dp[0] = True
        
        if sum >= arr[0]:
            dp[arr[0]] = True
        
        for idx in range(1, n):
            temp = [False for _ in range(sum+1)]
            
            for target in range(1, sum+1):
                if target >= arr[idx]:
                    take = dp[target - arr[idx]]
                else:
                    take = False
                
                dont_take = dp[target]
                
                temp[target] = take or dont_take
            
            dp = temp
            dp[0] = True
        
        return dp[sum]