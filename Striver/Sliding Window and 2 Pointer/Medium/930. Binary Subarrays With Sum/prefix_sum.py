# Similary: Subarray sum equal to k

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)

        dic = {0 : 1}

        cur_sum = 0

        sum_subarray = 0

        for i in range(len(nums)):
            cur_sum += nums[i]

            prefix_sum = cur_sum - goal

            if prefix_sum in dic:
                sum_subarray += dic[prefix_sum]
            

            if cur_sum in dic:
                dic[cur_sum] += 1
            else:
                dic[cur_sum] = 1
        
        return sum_subarray