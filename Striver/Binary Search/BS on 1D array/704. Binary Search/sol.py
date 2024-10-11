'''
https://www.youtube.com/watch?v=pPiSMPWKZ3E&t=120s&ab_channel=OggiAI-ArtificialIntelligenceToday

    Note that upper_bound and bisect.bisect_right look for the rightmost insertion position, 
    while lower_bound and bisect.bisect_left look for the leftmost insertion position.

    Right most insertion point is = Insert after a idx . Insert at correct position
    Left Most Insertion point is = Insert after a idx . Insert at correct position
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        left = 0
        right = n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            # print(mid)
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1

