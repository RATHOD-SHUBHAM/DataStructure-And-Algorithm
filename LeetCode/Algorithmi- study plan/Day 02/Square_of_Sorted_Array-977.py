'''

977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]



'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #base case
        if not nums or len(nums) == 0:
            return []
        
        
        ans = [0]*len(nums)
        left = 0
        right = len(nums) - 1
        
        pointer = right
        
        while left <= right:
            lftsqr = nums[left] * nums[left]
            rgtsqr = nums[right] * nums[right]
            
            if lftsqr <= rgtsqr:
                ans[pointer] = rgtsqr
                right -= 1
                pointer -=1
                
                
            else:
                ans[pointer] = lftsqr
                pointer -= 1
                left += 1
                
        return ans