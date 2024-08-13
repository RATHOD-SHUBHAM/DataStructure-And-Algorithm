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

        