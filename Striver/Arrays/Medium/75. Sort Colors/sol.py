'''
# The problem is known as Dutch National Flag Problem

Three pointer is needed:
    1. To keep track of all the 2 in the end.
    2. To keep track of all the 0 in the beginning.
    3. To keep moving from left to right

Place the pointers:
    1. Put all the 2 to the end and move the right pointer.
    2. Put all the zero at zero pointer and then move the zero pointer
    3. When there is one - Just proceed since the above two pointer will take care of one
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 

        zero_pointer = 0
        left = 0
        right = n - 1
        
        while left <= right:
            cur_num = nums[left]

            if cur_num == 0:
                # put it at a position where zero pointer will be pointing
                nums[zero_pointer] , nums[left] = nums[left] , nums[zero_pointer]
                zero_pointer += 1
                left += 1
            
            elif cur_num == 2:
                # place the 2 at correct position
                nums[left] , nums[right] = nums[right] , nums[left]
                right -= 1

            else:
                left += 1
        
        return nums