"""
Consider [2,3,2]:
    * Without breaking, we might naively choose both houses 1 and 3 (values 2 and 2) for a total of 4
    * But houses 1 and 3 are adjacent in the circle, so this would trigger the alarm!

By breaking the circle into:
    [2,3] (excluding the last house)
    [3,2] (excluding the first house)

We correctly handle both possibilities:
    * Rob house 1 but not house 3: [2,3] → optimal is 2
    * Rob house 3 but not house 1: [3,2] → optimal is 3

The maximum is 3, which is the correct answer.
This is why we need to break the circle - it's the only way to properly handle the constraint that the first and last houses are adjacent.RetryClaude does not have the ability to run the code it generates yet.Claude can make mistakes. Please double-check responses.


Also, the "breaking the circle" approach will always work for problems involving a circular arrangement with adjacent constraints
"""

class Solution:
    def recursion(self, n, nums):
        if n < 0:
            return 0
        
        if n == 0:
            return nums[0]
        
        pick = nums[n] + self.recursion(n-2, nums) # Cannot moce to adjacent house
        not_pick = 0 + self.recursion(n-1, nums) # If we dont pick current house, we can move to adjacent house

        return max(pick, not_pick)

    def house_robber_1(self, nums: List[int]) -> int:
        n = len(nums)
        return self.recursion(n-1, nums)
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return nums[0]
        
        """
        When houses are in a circle, breaking the circle is a common approach. By dividing the array into two subarrays as shown:

        num_1 = nums[0 : n-1] (includes first house but excludes last house)
        num_2 = nums[1: n] (excludes first house but includes last house)

        """

        num_1 = nums[0 : n-1]
        num_2 = nums[1: n]

        return max(self.house_robber_1(num_1), self.house_robber_1(num_2))
        