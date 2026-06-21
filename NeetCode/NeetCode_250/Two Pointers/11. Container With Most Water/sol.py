'''
Formula:
Height = Min(l, r)
Width = r - l

Area = h * w

Max(Area)


Movement:
if height[left] < height[right]:
    l += 1 // we want to increase area - so we will try increasing height of small building
else:
    r -= 1
'''

# Tc: O(n) | Sc: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        left = 0
        right = n - 1

        max_area = -math.inf

        while left < right:

            # Formula
            h = min(height[left], height[right])
            w = right - left

            a = h * w

            max_area = max(max_area, a)

            # Movement
            if height[left] < height[right]: # we want to increase area - so we will try increasing height of small building
                left += 1
            else:
                right -= 1
        
        return max_area
        