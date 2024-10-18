# Tc: O(n) | Sc: O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor