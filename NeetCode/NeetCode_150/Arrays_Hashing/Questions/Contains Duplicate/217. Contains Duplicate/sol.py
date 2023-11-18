# Tc: O(n) | Sc: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        set_len = len(set(nums))

        if n == set_len:
            return False
        else:
            return True