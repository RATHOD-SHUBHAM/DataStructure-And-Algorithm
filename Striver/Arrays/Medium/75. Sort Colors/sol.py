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

        p0 = 0 # keep track of 0
        left = 0
        right = n - 1 # Keep track of 2

        while left <= right:
            if nums[left] == 2:
                val = self.swap(left, right, nums)
                right -= 1
            elif nums[left] == 0:
                self.swap(left, p0, nums)
                p0 += 1
                left += 1
            else:
                left += 1
        
        return nums