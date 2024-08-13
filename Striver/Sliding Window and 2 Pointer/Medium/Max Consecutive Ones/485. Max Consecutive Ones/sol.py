class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)

        count = 0
        max_count = 0

        for i in range(n):
            if nums[i] == 0:
                count = 0
                continue
            
            count += 1
            max_count = max(max_count, count)
        
        return max_count