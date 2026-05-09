class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)

        for i, val in enumerate(nums):
            # Loop through rest of the array

            for j in range(i+1, min(i + indexDiff + 1 , n)): 
                # min(i + indexDiff + 1 , n): which ever occurs first: either the end of array or index difference that exceeds indexDiff criteria
                if abs(val - nums[j]) <= valueDiff:
                    return True
        
        return False


