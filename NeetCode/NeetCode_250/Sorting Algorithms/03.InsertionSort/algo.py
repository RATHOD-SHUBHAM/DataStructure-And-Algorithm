"""
Inserttion Sort: 
Core Idea: 
Think of how you sort playing cards in your hand. 
You pick one card at a time and insert it into its correct position among the already sorted cards. 
The left side is always sorted, and you grow it one element at a time by inserting the next element in the right place.

Tc and Sc: O(n^2)
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Start from the second element, first element alone is trivially sorted
        for i in range(1, n):
            key = nums[i] # Save the element to be inserted
            
            # Compare key with elements to its left, moving backwards
            j = i-1
            while j >= 0 and key < nums[j]:
                # shift every element that is greater than the key one position to the right
                nums[j+1] = nums[j]
                j -= 1
            
            # Place key in its correct position
            nums[j+1] = key

        return nums