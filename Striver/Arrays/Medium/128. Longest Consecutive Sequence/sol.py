class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        n = len(nums)

        LCS = 0

        for i in range(n):
            cur_num = nums[i]

            if cur_num - 1 in num_set:
                continue
            
            count = 0
            while cur_num in num_set:
                count += 1
                cur_num += 1

            LCS = max(LCS, count)
            
        return LCS