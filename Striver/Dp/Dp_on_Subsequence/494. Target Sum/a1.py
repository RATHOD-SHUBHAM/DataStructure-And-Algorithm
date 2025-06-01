class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        idx = n - 1

        cur_sum = 0

        return self.recursion(idx, cur_sum, nums, target)
    
    def recursion(self, idx, cur_sum, nums, target):
        if idx < 0:
            if cur_sum == target:
                return 1
            else:
                return 0
        
        # Take +
        take_pos = self.recursion(idx - 1, cur_sum + nums[idx], nums, target)

        # Take - 
        take_neg = self.recursion(idx - 1, cur_sum - nums[idx], nums, target)

        return take_pos + take_neg

# -------------------------------- Better Approach --------------------------------
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        idx = n - 1

        cur_sum = 0

        memo = {}

        return self.recursion(idx, cur_sum, memo, nums, target)
    
    def recursion(self, idx, cur_sum, memo, nums, target):
        if idx < 0:
            if cur_sum == target:
                return 1
            else:
                return 0
            
        if (idx, cur_sum) in memo:
            return memo[(idx, cur_sum)]
        
        # Take +
        take_pos = self.recursion(idx - 1, cur_sum + nums[idx], memo, nums, target)

        # Take - 
        take_neg = self.recursion(idx - 1, cur_sum - nums[idx], memo, nums, target)

        memo[(idx, cur_sum)] = take_pos + take_neg

        return memo[(idx, cur_sum)]

# -------------------------------- Recursion with Pattern Observation --------------------------------
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        """
        We know , 
        we can divide the array into two s1, s2

        We know s1 + s2 = total -> eq1

        We also know we need to assign positive and negative to array,
        so we assign +s1 and -s2

        From here we know 

        s1 - s2 = target -> eq 2

        From eq1 and eq2
        s1 + s2 = total
        s1 - s2 = target

        s1 = total - s2

        s1 - total + s1 = target

        2 * s1 = target + total

        s1 = (target + total) // 2


        """

        total = sum(nums)

        # We cannot divide the array into 2 halves
        if (target + total) % 2 != 0 or (target > total):
            return 0

        new_target = (total + target) // 2

        idx = n - 1

        return self.recursion(idx, new_target, nums)

    def recursion(self, idx, target, arr):
        # base case
        if idx < 0:
            if target == 0:
                return 1
            else:
                return 0
            
        # Logic
        if arr[idx] <= target:
            take = self.recursion(idx - 1, target - arr[idx], arr)
        else:
            take = 0
        
        no_take = self.recursion(idx - 1, target, arr)

        return take + no_take

# -------------------------------- Memoization  --------------------------------
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        total = sum(nums)

        # We cannot divide the array into 2 halves
        if (target + total) % 2 != 0 or (target > total):
            return 0

        new_target = (total + target) // 2

        idx = n - 1

        memo = {}

        return self.recursion(idx, memo, new_target, nums)

    def recursion(self, idx, memo, target, arr):
        # base case
        if idx < 0:
            if target == 0:
                return 1
            else:
                return 0
        
        if (idx, target) in memo:
            return memo[(idx, target)]
            
        # Logic
        if arr[idx] <= target:
            take = self.recursion(idx - 1, memo, target - arr[idx], arr)
        else:
            take = 0
        
        no_take = self.recursion(idx - 1, memo, target, arr)

        memo[(idx, target)] = take + no_take

        return memo[(idx, target)]

# -------------------------------- Tabulation  --------------------------------
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # write your code here
        total_sum = sum(nums)

        """
        Edge Cases:
        1. (S + D) must be even - otherwise no valid partition exists
        2. D < S difference can't be larger than total sum
        """

        if (total_sum + target) % 2 != 0 or (abs(target) > total_sum):
            return 0
        
        """
        If we consider s2 to be our target
        if (total_sum - d) % 2 != 0 or (total_sum - d < 0):
            return 0
        """

        new_target = (total_sum + target) // 2
        

        return self.findWays(nums, new_target)

    def findWays(self, arr, target):
        n = len(arr)

        dp = [[0 for _ in range(target + 1)]for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1
        

        if arr[0] == 0:
            dp[0][0] = 2
        else:
            if arr[0] <= target:
                dp[0][arr[0]] = 1
        
        for idx in range(1, n):
            for cur_sum in range(target + 1):
                if cur_sum >= arr[idx]:
                    take = dp[idx-1][cur_sum - arr[idx]]
                else:
                    take = 0
                
                no_take = dp[idx-1][cur_sum]
            
                dp[idx][cur_sum] = take + no_take
        
        return dp[n-1][target]

# -------------------------------- Space Optimization  --------------------------------
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # write your code here
        total_sum = sum(nums)

        """
        Edge Cases:
        1. (S + D) must be even - otherwise no valid partition exists
        2. D < S difference can't be larger than total sum
        """

        if (total_sum + target) % 2 != 0 or (abs(target) > total_sum):
            return 0
        
        """
        If we consider s2 to be our target
        if (total_sum - d) % 2 != 0 or (total_sum - d < 0):
            return 0
        """

        new_target = (total_sum + target) // 2
        

        return self.findWays(nums, new_target)

    def findWays(self, arr, target):
        n = len(arr)

        dp = [0 for _ in range(target + 1)]
        

        if arr[0] == 0:
            dp[0] = 2
        else:
            dp[0] = 1
            if arr[0] <= target:
                dp[arr[0]] = 1
        
        for idx in range(1, n):
            temp = [0 for _ in range(target + 1)]

            for cur_sum in range(target + 1):
                if cur_sum >= arr[idx]:
                    take = dp[cur_sum - arr[idx]]
                else:
                    take = 0
                
                no_take = dp[cur_sum]
            
                temp[cur_sum] = take + no_take
            
            dp = temp
        
        return dp[target]