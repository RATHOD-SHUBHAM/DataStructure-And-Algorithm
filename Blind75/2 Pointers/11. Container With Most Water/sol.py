# Tc: O(n) | Sc: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        max_area = -math.inf

        left = 0
        right = n - 1

        while left < right:
            length = min(height[left], height[right])
            breath = right - left

            area = length * breath

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
    
        return max_area




