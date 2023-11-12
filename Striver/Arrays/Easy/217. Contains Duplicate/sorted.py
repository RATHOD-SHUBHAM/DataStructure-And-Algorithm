# Tc: O(nlogn) | Sc: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        sorted_nums = sorted(nums)

        for i in range(1, n):
            if sorted_nums[i-1] == sorted_nums[i]:
                return True
        
        return False