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