# Time: O(n)
# Sc : O(1)

class Solution:
    def swap(self, i, j , nums):
        nums[i] , nums[j] = nums[j] , nums[i]
            
    def reverse(self, nums, left, right):
        while left < right:
            self.swap(left, right, nums)
            left += 1
            right -= 1
        return nums
            
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # base case
        if n <= 1:
            return nums
        
        # pointer which says where the number should be swapped
        div_pointer = n - 2
        
        while div_pointer >= 0 and nums[div_pointer] >= nums[div_pointer + 1]:
            div_pointer -= 1
            
        # print(div_pointer)
        # either my divider will be outside 0 or i would have found my division point
        if div_pointer < 0:
            return self.reverse(nums, 0 , n -1)
        else:
            # get the element that is greater than current element by smallest in the division subset
            for i in reversed(range(div_pointer + 1 , n)):
                if nums[div_pointer] < nums[i]:
                    self.swap(div_pointer , i , nums)
                    break
            
            # now reverse the remaining value
            self.reverse(nums, div_pointer+ 1 , n - 1)
            
            # return nums (we dont have to return anything)
        
        
        
        
        
        
            