'''
# Dutch national land problem.

# The problem is known as Dutch National Flag Problem

Three pointer is needed:
    1. To keep track of all the 2 in the end.
    2. To keep track of all the 0 in the beginning.
    3. To keep moving from left to right

Place the pointers:
    1. Put all the 2 to the end and move the right pointer.
    2. Put all the zero at zero pointer and then move the zero pointer
    3. When there is one - Just proceed since the above two pointer will take care of one

Summary:
    1. p0 -> Places all the 0s in the right position.
    2. right -> Places all the 1s in the right position.
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        left = 0 # keep track of 0's
        p = 0
        right = n - 1 # keep track of 2's

        while p <= right:
            if nums[p] == 0:
                self.swap(p, left, nums)
                left += 1
                p += 1
            elif nums[p] == 2:
                self.swap(p, right, nums)
                right -= 1
            else:
                p += 1
        
        return nums
    
    def swap(self, x, y, nums):
        nums[x], nums[y] = nums[y], nums[x]