'''
If target is not found:
    * It return the index to be inserted at.

If target is found:
    * bisect_right : return the right index.
    * bisect_left : return the left index.
'''
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_right(nums, target)

        print(idx) # The targe correct position is this index

        if idx > 0 and nums[idx - 1] == target:
            return idx - 1
        else:
            return -1