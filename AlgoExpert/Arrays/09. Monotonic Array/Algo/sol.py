# Time and Space: O(n) | O(1)
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # initially I dont know weather the number is increasing or decreasing
        increasing = False
        decreasing = False
        
        # if both flip: Meaning it is both increasing and decresing
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                increasing = True
            elif nums[i] < nums[i-1]:
                decreasing = True
        
        # both flipped: Meaning numbers increased and decreased
        if increasing== True and decreasing == True: 
            return False
        else:
            return True