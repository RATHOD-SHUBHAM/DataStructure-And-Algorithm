class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # Brute Force
        for i , val in enumerate(nums):
            for j in range(i+1, min(i+1+indexDiff , len(nums))):
                if abs(val - nums[j]) <= valueDiff:
                    return True
        return False