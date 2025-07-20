class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        # Pad the original list with 1 at both ends to handle edge boundaries easily
        nums = [1] + nums + [1]

        # We solve the problem in the range [1, n] because 0 and n+1 are dummy boundaries
        i = 1
        j = n

        return self.recursion(i, j, nums)
    
    def recursion(self, i, j, nums):
        # Base case: if the subarray is invalid (no balloons to burst), return 0 coins
        if i > j:
            return 0
        
        # Initialize the maximum coins for this subproblem
        maxi = -math.inf

        # Try bursting each balloon 'idx' as the last one in the range [i, j]
        for idx in range(i, j + 1):
            # Recursively solve for the left and right partitions
            left_subprob = self.recursion(i, idx - 1, nums)
            right_subprob = self.recursion(idx + 1, j, nums)

            # Calculate coins for bursting 'idx' last in this range
            # Neighbors are fixed: nums[i-1] and nums[j+1]
            cur_cost = nums[i - 1] * nums[idx] * nums[j + 1]

            # Total coins = left + right + coins from bursting current balloon last
            total_cost = left_subprob + right_subprob + cur_cost

            # Keep track of the maximum coins from all choices
            maxi = max(maxi, total_cost)
        
        # Return the best result for bursting all balloons in range [i, j]
        return maxi
