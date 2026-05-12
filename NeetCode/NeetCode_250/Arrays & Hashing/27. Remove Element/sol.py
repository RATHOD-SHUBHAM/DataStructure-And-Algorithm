# Tc: O(n) | Sc: O(1)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)

        i = 0
        j = n - 1

        while i <= j:
            if nums[i] == val:
                self.swap(i, j, nums)
                j -= 1
            else:
                i += 1
            
            print(nums)
        
        return i
    
    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]

"""
nums = [2, 1], val = 2
"""