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
