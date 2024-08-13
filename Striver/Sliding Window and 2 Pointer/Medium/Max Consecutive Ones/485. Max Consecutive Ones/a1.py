# ------------------- While Loop -------------------

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)

        max_len = 0

        left = right = 0

        while right < n:
            cur_num = nums[right]

            if cur_num == 0:
                cur_len = right - left
                max_len = max(cur_len, max_len)
                left = right + 1
            
            right += 1

        cur_len = right - left
        max_len = max(cur_len, max_len)
        
        return max_len
    

# ------------------- For Loop -------------------

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