class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)

        for i in range(n):
            xor ^= nums[i]
        
        return xor