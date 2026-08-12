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

# ======================================== In simple terms ============================================
# Study Equation before solving


# Window will always hold elements that are with in the range of indexDiff
# From this Window , we need to select element that are with in range of valueDiff
# From deriving abs(nums[i] - nums[j]) <= valueDiff, we know that (num - x) <= valueDiff -> num - valueDiff -------- x -------- num + valueDiff
                                                                                            # (low)                                (high)
# if we do binary search on low, we will get a value(x), where all the element to right of it is > low
# So this value(x) will always be >= low
# Next we need to check if this abs(num - value(x)) <= valueDIff
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = SortedSet() # Keep track of current number in window
        # Sort it because, Sorted lets us jump straight to the right spot, like we know every number to left is smaller and to right is bigger, atleast this gives us an idea


        ptr = 0 # this will help is shrink the window
        # this will point to element of nums and not window


        for num in nums:
            range = [num - valueDiff, num + valueDiff] # this we got from the equation we solved
            # so our range is num - valueDiff -------- x -------- num + valueDiff
                                # (low)                                (high)

            # lets choose the low
            pos = window.bisect_left(range[0]) # so this will tell us that, for sure that any number at or to the right of pos in window will be >= nums - valueDiff (low)

            # now we need to check if number is <= high
            if pos < len(window) and abs(num - window[pos]) <= valueDiff:
                return True

            # Add to window
            window.add(num)

            # Shrink window if needed
            if len(window) > indexDiff:
                window.remove(nums[ptr])
                ptr += 1
        
        return False

