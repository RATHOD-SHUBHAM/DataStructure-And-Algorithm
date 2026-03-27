class Solution:
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        ptr = 0
        red = 0 # color 0
        blue = n - 1 # color 2

        while ptr <= blue:
            if nums[ptr] == 2:
                # swap with blue, move blue backward (don't move ptr)
                self.swap(nums, ptr, blue)
                blue -= 1
            
            elif nums[ptr] == 0:
                # swap with red, move both red and ptr forward
                self.swap(nums, ptr, red)
                red += 1
                ptr += 1
            
            else:
                # white's in the right place, just move ptr forward
                ptr += 1

        return nums