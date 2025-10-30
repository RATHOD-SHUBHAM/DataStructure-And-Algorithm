'''
https://www.youtube.com/watch?v=pPiSMPWKZ3E&t=120s&ab_channel=OggiAI-ArtificialIntelligenceToday

    Note that upper_bound and bisect.bisect_right look for the rightmost insertion position, 
    while lower_bound and bisect.bisect_left look for the leftmost insertion position.

    Right most insertion point is = Insert after a idx . Insert at correct position
    Left Most Insertion point is = Insert after a idx . Insert at correct position
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_right(nums, target)

        print(idx) # The targe correct position is this index

        if idx > 0 and nums[idx - 1] == target:
            return idx - 1
        else:
            return -1