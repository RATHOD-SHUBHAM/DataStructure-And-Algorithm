# Tc: O(n), n is the number of elements in nums
# Sc: O(1)

# Two Pointer
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)

        ptr = 0
        end = n - 1

        while ptr <= end:
            if nums[ptr] == val:
                # Swap the values
                nums[ptr], nums[end] = nums[end], nums[ptr]
                end -= 1 # Decrement the end, as we know for sure that is a val
            else:
                ptr += 1
                # This is a number that is not a val
        
        return ptr

