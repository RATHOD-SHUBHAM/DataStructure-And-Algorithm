# Tc: O(n^2) | Sc: O(1)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        max_area = -math.inf

        for i in range(n):
            min_height = heights[i] # keeps track of smallest building

            for j in range(i, n):
                # length = the distance between i and j, breadth = minimum height building
                min_height = min(min_height, heights[j])
                length = j - i + 1
                
                cur_area = length * min_height

                max_area = max(max_area , cur_area)
        
        return max_area
        