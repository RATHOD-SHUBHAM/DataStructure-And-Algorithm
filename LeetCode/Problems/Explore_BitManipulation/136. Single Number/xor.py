class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        xor = 0
        for i in range(n):
            cur_num = nums[i]
            xor ^= cur_num
        
        return xor