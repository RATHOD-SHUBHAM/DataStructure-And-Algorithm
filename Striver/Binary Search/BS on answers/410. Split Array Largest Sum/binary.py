class Solution:
    def checkSplit(self, split, nums, k , n):
        '''Check how many K can be formed with current split'''
        projected_k_value = 1
        cur_split_val = 0

        for i in range(n):
            if cur_split_val + nums[i] <= split:
                cur_split_val += nums[i]
            else:
                cur_split_val = nums[i]
                projected_k_value += 1
        
        # print(split, projected_k_value)
        return projected_k_value

    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n < k:
            return -1

        left = max(nums) # to form a subarray, the min value a subarray with one value, it can hold is the max value
        right = sum(nums) # Entire array can be considered to be one subarray

        min_split = -1

        while left <= right:
            split = left + (right - left) // 2

            # Check how many k can be formed with current split
            projected_k_value = self.checkSplit(split, nums, k , n)

            if projected_k_value <= k:
                right = split - 1
                min_split = split
            else:
                left = split + 1
        
        return min_split
            


