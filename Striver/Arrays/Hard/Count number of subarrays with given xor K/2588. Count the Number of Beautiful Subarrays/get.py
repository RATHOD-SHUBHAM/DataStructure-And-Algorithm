class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        dic = {0 : 1}

        xor = count = 0

        for i in range(n):
            xor ^= nums[i]
            count += dic.get(xor, 0)
            dic[xor] = dic.get(xor, 0) + 1
        
        return count