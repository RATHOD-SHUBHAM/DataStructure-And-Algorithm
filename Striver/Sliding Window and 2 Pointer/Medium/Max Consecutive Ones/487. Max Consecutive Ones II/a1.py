from typing import List
import math

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)

        dic = {}

        left = right = 0 # Window

        max_len = -math.inf

        while right < n:
            cur_num = nums[right]

            if cur_num == 0:
                if cur_num in dic:
                    """
                        If some zero previously was already flipped. Slide window forward by removing that.
                    """
                    cur_len = right - left
                    max_len = max(cur_len, max_len)

                    left = dic[cur_num] + 1
                    dic[cur_num] = right
                else:
                    dic[cur_num] = right
            
            right += 1
        
        cur_len = right - left
        max_len = max(cur_len, max_len)

        return max_len

# ----------  Same Solution modified code  ------------------

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)

        dic = {}

        left = right = 0

        max_len = -math.inf

        while right < n:
            cur_num = nums[right]

            if cur_num == 0:
                
                if cur_num in dic:
                    cur_len = right - left
                    max_len = max(cur_len, max_len)
                    left = dic[cur_num] + 1
                    
                dic[cur_num] = right
            
            right += 1
        
        cur_len = right - left
        max_len = max(cur_len, max_len)

        return max_len
    
# ----------  2 pointer in different way  ------------------

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)

        dic = {}

        left = right = 0

        max_len = 0

        while right < n:
            cur_num = nums[right]

            if cur_num == 0:
                if cur_num not in dic:
                    dic[cur_num] = right
                else:
                    left = dic[cur_num] + 1
                    dic[cur_num] = right
            
            cur_len = right - left + 1

            max_len = max(max_len , cur_len)

            right += 1
        
        return max_len       

# ----------  Prefix Sum  ------------------

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)

        cur_sum = 0 # total running sum
        prev_sum = 0 # Sum upto the previous zero

        cur_sum = max_sum = 0

        for num in nums:
            cur_sum += 1

            if num == 0:
                '''
                a + b = X
                b = X - a
                '''
                cur_sum = cur_sum - prev_sum # Window sum between 2 0s
                prev_sum = cur_sum
            
            max_sum = max(max_sum , cur_sum)
        
        return max_sum