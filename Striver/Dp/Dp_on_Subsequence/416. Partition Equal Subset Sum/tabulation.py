class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        half_sum = total_sum // 2

        dp = [[False for _ in range(half_sum + 1)] for _ in range(n)]

        # Base case
        for i in range(n):
            dp[i][0] = True

        """
        dp[0][nums[0]] = True (if half_sum >= nums[0]): This sets that using only the first element (at index 0), we can form a sum equal to its value nums[0]. 
        The check half_sum >= nums[0] ensures we don't access an out-of-bounds index in the dp table.
        """
        if half_sum >= nums[0]:
            dp[0][nums[0]] = True

        # Logic
        """
        This nested loop is filling out a dynamic programming table where:

        dp[idx][cur_sum] represents whether it's possible to form a subset with cur_sum using any combination of elements from index [0 to idx] in the nums array.

        For each number at index [idx] and each possible cur_sum, the algorithm considers two options:
            * Take the current number (take): If we include the current number nums[idx] in our subset, we need to check if we could form cur_sum - nums[idx] using elements from index 0 to idx-1. This is only possible if cur_sum is at least as large as nums[idx].
            * Don't take the current number (dont_take): If we exclude the current number, we check if we could already form cur_sum using only elements from index 0 to idx-1.
        """
        for idx in range(1, n):
            for cur_sum in range(1, half_sum + 1):
                if cur_sum >= nums[idx]:
                    take = dp[idx - 1][cur_sum - nums[idx]]
                else:
                    take = False
                
                dont_take = dp[idx - 1][cur_sum]

                dp[idx][cur_sum] = take or dont_take
        
        return dp[n-1][half_sum]
