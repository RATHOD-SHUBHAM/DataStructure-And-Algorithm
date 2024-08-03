# keep track of the subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        new_start = 0 # keep track of where the new start position would be
        
        # keep track of the max window subarray
        left = 0
        right = 0


        cur_sum = 0
        max_sum = -math.inf

        for i in range(n):
            if cur_sum == 0:
                # might be start of new subarray
                new_start = i
            
            # create a max sum window
            cur_sum += nums[i]
            
            if cur_sum > max_sum:
                max_sum = cur_sum

                left = new_start
                right = i

            # if we see sum going below 0 - we reset new start, so we make cur_sum as 0. This means the current subarray will not help in creating a max_subarray
            if cur_sum < 0:
                cur_sum = 0

        print(nums[left : right + 1]) 
        return max_sum



# ------------------- Algo -----------------------

# Kadanes - Just give the max sum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        max_subarray_sum = cur_sum = nums[0]

        for i in range(1, n):
            cur_sum = max(nums[i] , cur_sum + nums[i])
            # print(cur_sum)
            max_subarray_sum = max(max_subarray_sum , cur_sum)
        
        return max_subarray_sum