# Tc: O(n) | Sc: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        maxArea = -math.inf

        left = 0
        right = n - 1

        while left < right:
            cur_height = min(height[left], height[right])
            cur_width = right - left

            area = cur_height * cur_width

            maxArea = max(area, maxArea)

            # move pointers - we need to increase height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea