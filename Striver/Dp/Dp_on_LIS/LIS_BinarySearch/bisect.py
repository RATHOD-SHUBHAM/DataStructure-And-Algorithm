"""
Intution :
    We are only conserned with the length of array
    and not the subsequency itself.

We need to memorize this logic
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []

        for num in nums:
            i = bisect.bisect_left(sub, num)

            if i == len(sub):
                sub.append(num)
            
            sub[i] = num
        
        return len(sub)
            

        