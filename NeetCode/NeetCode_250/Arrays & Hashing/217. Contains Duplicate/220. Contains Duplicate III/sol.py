from bisect import bisect_left
from sortedcontainers import SortedSet

"""
https://www.youtube.com/watch?v=HVh6u2Rf4P4
bisect_left module performs a binary search on a sorted list to find an insertion point on left.
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = SortedSet()

        left = 0
        
        for num in nums:
            # Find potential candidate near num
            pos = window.bisect_left(num - valueDiff)

            # Check if number in window within [num - valueDiff, num + valueDiff]
            if pos < len(window) and abs(window[pos] - num) <= valueDiff:
                return True
            
            # Add current number to window
            window.add(num)

            # Maintain window size <= indexDiff
            if len(window) > indexDiff:
                window.remove(nums[left])
                left += 1
        
        return False