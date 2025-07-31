# brute force
# Tc: O(n^3) | Sc: O(1)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        max_area = -math.inf

        for i in range(n):
            for j in range(i, n):
                
                min_height = heights[i] # keeps track of smallest building
                for k in range(i, j+1):
                    min_height = min(min_height, heights[k])
                
                # length = the distance between i and j, breadth = minimum height building
                length = j - i + 1
                cur_area = length * min_height

                max_area = max(max_area , cur_area)
        
        return max_area
        