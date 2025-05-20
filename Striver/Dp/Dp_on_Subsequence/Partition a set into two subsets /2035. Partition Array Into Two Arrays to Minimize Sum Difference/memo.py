class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        m = n // 2  # We need two arrays of equal length, ie 'n'
        total = sum(nums)  # The actual sum, not the sum of absolute values

        idx = n - 1
        count = 0
        current_sum = 0

        memo = {}

        return self.recursion(idx, count, current_sum, memo, m, n, total, nums)

        
    def recursion(self, idx, count, current_sum, memo, m, n, total, nums):
        # Base case
        # If we've processed all elements but haven't selected n elements, return infinity
        if idx < 0:
            return math.inf
        
        # If we've already selected n elements, calculate the difference
        if count == m:
            # current_sum represents the sum of array1
            arr_1 = current_sum
            # total - current_sum represents the sum of array2
            arr_2 = total - arr_1
            return abs(arr_1 - arr_2)
        
        if (idx, count, current_sum) in memo:
            return memo[(idx, count, current_sum)]
            
            
        # Two choices: either include nums[index] in array1 or array2
        # Include in array1 (add to current_sum)
        take = self.recursion(idx - 1, count + 1, current_sum + nums[idx], memo, m, n, total, nums)
        
        # Include in array2 (don't add to current_sum)
        no_take = self.recursion(idx - 1, count, current_sum, memo, m, n, total, nums)
        
        memo[(idx, count, current_sum)] = min(take, no_take)

        return memo[(idx, count, current_sum)]