# ------------------------------------- Recursive Solution -------------------------------------
# Time Complexity: O(2^n)
# Space Complexity: O(n) for recursion stack

class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        n = len(arr)
        
        idx = n - 1
        
        return self.recursion(idx, arr, sum)
    
    def recursion(self, idx, arr, target):
        # base case
        if idx == 0:
            if target == 0:
                return True
                
            if arr[0] == target:
                return True
            else:
                return False
        
        # Take
        if arr[idx] <= target:
            take = self.recursion(idx - 1, arr, target - arr[idx])
        else:
            take = False
        
        no_take = self.recursion(idx - 1, arr, target)
        
        return take or no_take
    
# ------------------------------------- Method 2: Memoization -------------------------------------
# Time Complexity: O(n * target)
# Space Complexity: O(n * target) for memoization table + O(n) for recursion stack

class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        n = len(arr)
        
        idx = n - 1
        
        memo = {}
        
        return self.recursion(idx, memo, arr, sum)
    
    def recursion(self, idx, memo, arr, target):
        # base case
        if idx == 0:
            if target == 0:
                return True
                
            if arr[0] == target:
                return True
            else:
                return False
        
        if (idx, target) in memo:
            return memo[(idx, target)]
        
        # Take
        if arr[idx] <= target:
            take = self.recursion(idx - 1, memo, arr, target - arr[idx])
        else:
            take = False
        
        no_take = self.recursion(idx - 1, memo, arr, target)
        
        memo[(idx, target)] =  take or no_take
        
        return memo[(idx, target)]


# ------------------------------------- Method 3: Tabulation -------------------------------------
# Time Complexity: O(n * target)
# Space Complexity: O(n * target)

class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        n = len(arr)
        
        dp = [[False for _ in range(sum+1)] for _ in range(n)]
        
        # base case
        for i in range(n):
            dp[i][0] = True
        
        if arr[0] <= sum:
            dp[0][arr[0]] = True
        
        for idx in range(1, n):
            for cur_sum in range(1, sum+1):
                # Take
                if arr[idx] <= cur_sum:
                    take = dp[idx - 1][cur_sum - arr[idx]]
                else:
                    take = False
                
                no_take = dp[idx - 1][cur_sum]
                
                dp[idx][cur_sum] = take or no_take
        
        return dp[n-1][sum]
    
# ------------------------------------- Method 4: Space Optimization -------------------------------------
# Time Complexity: O(n * target)
# Space Complexity: O(target)

class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        n = len(arr)
        
        dp = [False for _ in range(sum+1)]
        
        # base case
        dp[0] = True
        
        if arr[0] <= sum:
            dp[arr[0]] = True
        
        # Logic
        for idx in range(1, n):
            temp = [False for _ in range(sum+1)]
            temp[0] = True
            
            for cur_sum in range(1, sum+1):
                # Take
                if arr[idx] <= cur_sum:
                    take = dp[cur_sum - arr[idx]]
                else:
                    take = False
                
                no_take = dp[cur_sum]
                
                temp[cur_sum] = take or no_take
            
            dp = temp
        
        return dp[sum]
        