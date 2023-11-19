# Tc: O(nlogn) Sc: O(1)
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        n = len(nums)
        
        left = 0
        right = n - 1
        
        max_sum = -1
        while left < right:
            summ = nums[left] + nums[right]
            
            if summ > k or summ == k:
                right -= 1
            else:
                max_sum = max(summ, max_sum)
                left += 1
        
        return max_sum

            
            