# Tc: O(n) | Sc: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        min_ele = nums[0]

        for i in range(1, n):
            if nums[i] < min_ele:
                min_ele = nums[i]
        
        return min_ele