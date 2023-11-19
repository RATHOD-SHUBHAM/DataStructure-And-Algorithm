# Tc: O(nlogn) and Sc: O(n)
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # sort to place them on x plane
        points.sort(key = lambda x : x[1])
        
        no_of_arrow = 1
        first_end= points[0][1]
        
        
        # if at any point of the points are non - overlapping then ill need a extra ballon
        for x_start , x_end in points:
            # adjust the new end point
            if x_start > first_end:
                no_of_arrow += 1
                first_end = x_end
                
        return no_of_arrow