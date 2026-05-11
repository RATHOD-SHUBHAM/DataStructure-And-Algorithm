# Index constraint  → guaranteed by notepad size (eviction keeps it honest)
# Value constraint  → checked by bisect_left + range check


from bisect import bisect_left
from sortedcontainers import SortedSet

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)

        notepad = SortedSet() # notepad will ONLY contains numbers from the last indexDiff steps.

        left = 0 # keep track of element in nums

        for num in nums:
            range = [num - valueDiff, num + valueDiff] # "Range check if:  ANY number sitting between num - valueDiff and num + valueDiff in my notepad?"
            # bisect_left(num - valueDiff) jumps to the first number that could "possibly" be in range.
            pos = notepad.bisect_left(range[0])

            if pos < len(notepad) and abs(num - notepad[pos]) <= valueDiff: # Check if this possible value falls in range of valueDiff
                return True
            

            # The eviction logic guarantees notepad has element in range of indexDiff
            notepad.add(num)

            if len(notepad) > indexDiff:
                notepad.remove(nums[left]) # remove OLDEST number from nums
                left += 1 # slide left forward
        
        return False
 

# try solving on paper
"""
1. nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3 -> False
2. nums = [4,1,6,3], indexDiff = 2, valueDiff = 2 -> True
3. nums = [1, 7, 3, 1, 9], indexDiff = 2, valueDiff = 1 -> False
4. nums = [1, 7, 3, 2, 9], indexDiff = 2, valueDiff = 1 -> True
"""