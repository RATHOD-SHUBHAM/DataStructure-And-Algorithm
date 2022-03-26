"""

977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].


"""
# Time and Space = O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_squares = [1] * len(nums)
        
        # assign pointers
        left = 0
        right = i = len(nums) - 1
        
        # move as long as left crosses right
        while left <= right:
            sqre_left = nums[left] ** 2
            sqre_right = nums[right] ** 2
            
            if sqre_left < sqre_right:
                sorted_squares[i] = sqre_right
                right -= 1
            else:
                sorted_squares[i] = sqre_left
                left += 1
                
            i -= 1
            
        return sorted_squares
        