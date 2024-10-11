# Tc: O(nlogn) | Sc: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)

        for i in range(1, n, 3):
            if nums[i] != nums[i-1]:
                return nums[i-1]
        
        return nums[-1]