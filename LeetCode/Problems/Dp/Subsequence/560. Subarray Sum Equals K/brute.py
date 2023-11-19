# Tc : O(n^2) |Sc: O(1)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        
        for i in range(n):
            sub_sum = 0
            for j in range(i , n):
                sub_sum += nums[j]
                
                if sub_sum == k:
                    count += 1
        
        return count