# -------------------------------------- 2 Pointers --------------------------------------


# Similar to : Count number of substrings

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        k = goal
        atmost_k = self.countSubarray(nums, k)
        atmost_k_minus_1 = self.countSubarray(nums, k-1)

        return atmost_k - atmost_k_minus_1
    
    def countSubarray(self, nums, k):
        n = len(nums)

        total_len = cur_sum = 0

        left = right = 0

        while right < n:
            cur_sum += nums[right]

            while left <= right and cur_sum > k:
                cur_sum -= nums[left]
                left += 1
            

            total_len += right - left + 1

            right += 1
        
        return total_len
    

# -------------------------------------- Prefix Sum --------------------------------------

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
