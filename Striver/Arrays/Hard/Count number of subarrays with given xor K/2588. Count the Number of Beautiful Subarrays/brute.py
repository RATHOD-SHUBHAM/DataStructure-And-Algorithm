class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1 and nums[0] == 0:
            return 1


        count = 0

        for i in range(n):
            xor = 0 ^ nums[i]

            for j in range(i+1, n):
                xor ^= nums[j]

                if xor == 0:
                    count += 1
        
        # print(count)
        return count