"""
Intution :
    We are only conserned with the length of array
    and not the subsequency itself.

We need to memorize this logic
"""

class Solution:
    def binary_search(self, num, sub):
        n = len(sub)

        left = 0
        right = n

        while left < right:
            mid = (right + left) // 2

            if sub[mid] < num:
                left = mid+1
            else:
                right = mid
        
        return left

    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []

        for num in nums:
            i = self.binary_search(num, sub)

            if i == len(sub):
                sub.append(num)
            
            sub[i] = num
        
        return len(sub)
            

        