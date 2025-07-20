class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        # Pad the original list with 1 at both ends to handle edge boundaries easily
        nums = [1] + nums + [1]

        dp = [[0 for _ in range(n+2)]for _ in range(n+2)]

        # We solve the problem in the range [1, n] because 0 and n+1 are dummy boundaries
        # i = 1 # 1- >n
        # j = n # n to 1

        for i in reversed(range(1, n+1)):
            for j in range(1, n+1):
                if i > j:
                    continue
                
                # Initialize the maximum coins for this subproblem
                maxi = -math.inf

                # Try bursting each balloon 'idx' as the last one in the range [i, j]
                for idx in range(i, j + 1):
                    # Recursively solve for the left and right partitions
                    left_subprob = dp[i][idx-1]
                    right_subprob = dp[idx+1][j]

                    # Calculate coins for bursting 'idx' last in this range
                    # Neighbors are fixed: nums[i-1] and nums[j+1]
                    cur_cost = nums[i - 1] * nums[idx] * nums[j + 1]

                    # Total coins = left + right + coins from bursting current balloon last
                    total_cost = left_subprob + right_subprob + cur_cost

                    # Keep track of the maximum coins from all choices
                    maxi = max(maxi, total_cost)
                
                dp[i][j] = maxi
        
        return dp[1][n]