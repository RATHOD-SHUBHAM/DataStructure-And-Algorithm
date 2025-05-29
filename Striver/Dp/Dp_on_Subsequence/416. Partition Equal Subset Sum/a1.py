# ------------------------------------ Recursion ------------------------------------

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2
        idx = n - 1
        
        return self.recursion(idx, nums, target)
    
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
        
        # No_take
        no_take = self.recursion(idx - 1, arr, target)
        
        return take or no_take
    
# ------------------------------------ Memoization ------------------------------------

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2
        idx = n - 1

        memo = {}

        return self.recursion(idx, memo, nums, target)
    
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
        
        memo[(idx, target)] = take or no_take

        return memo[(idx, target)]
    
# ------------------------------------ Tabulation ------------------------------------

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2
        
        dp = [[False for _ in range(target+1)] for _ in range(n)]
        
        # base case
        for i in range(n):
            dp[i][0] = True
        
        if nums[0] <= target:
            dp[0][nums[0]] = True
        
        for idx in range(1, n):
            for cur_sum in range(1, target+1):
                # Take
                if nums[idx] <= cur_sum:
                    take = dp[idx - 1][cur_sum - nums[idx]]
                else:
                    take = False
                
                no_take = dp[idx - 1][cur_sum]
                
                dp[idx][cur_sum] = take or no_take
        
        return dp[n-1][target]
    
# ------------------------------------ Space Optimization ------------------------------------

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2
        
        dp = [False for _ in range(target+1)]
        
        # base case
        dp[0] = True
        
        if nums[0] <= target:
            dp[nums[0]] = True
        
        # Logic
        for idx in range(1, n):
            temp = [False for _ in range(target+1)]
            temp[0] = True
            
            for cur_sum in range(1, target+1):
                # Take
                if nums[idx] <= cur_sum:
                    take = dp[cur_sum - nums[idx]]
                else:
                    take = False
                
                no_take = dp[cur_sum]
                
                temp[cur_sum] = take or no_take
            
            dp = temp
        
        return dp[target]