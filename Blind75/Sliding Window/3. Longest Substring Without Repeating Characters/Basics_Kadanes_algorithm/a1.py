# Tc: O(n^3) | Sc: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_subarray_sum = -math.inf
        
        for i in range(n):
            for j in range(i, n):
                cur_sum = 0

                for k in range(i, j+1):
                    cur_sum += nums[k]
                    max_subarray_sum = max(max_subarray_sum , cur_sum)
        
        return max_subarray_sum
    
# ------------------------------------------------------------------------

# Tc: O(n^2) | Sc: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_subarray_sum = -math.inf
        
        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum += nums[j]

                max_subarray_sum = max(max_subarray_sum , cur_sum)
            
        return max_subarray_sum
    
# ------------------------------------------------------------------------


# Tc: O(n) | Sc: O(1)

# Kadens Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_subarray_sum = cur_sum = nums[0]

        for i in range(1, n):
            cur_sum = max(nums[i] , cur_sum + nums[i])
            max_subarray_sum = max(max_subarray_sum , cur_sum)
        
        return max_subarray_sum