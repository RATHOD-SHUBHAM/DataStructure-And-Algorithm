# TC: O(N^2) | Sc: O(N)

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # store all the points on graph
        points_on_axis = set()
        min_area = math.inf
        
        # for every points
        for x1 , y1 in points:
            # compare with the previous points
            for x2 , y2 in points_on_axis:
                # check if the diagonal value exist - if it does then we have a triangle
                # diagonals = x1y2 , x2y1
                if (x1,y2) in points_on_axis and (x2,y1) in points_on_axis:
                    area = abs(x2-x1) * abs(y2 - y1)
                    min_area = min(min_area , area)
                    
            # add the new point to the set
            points_on_axis.add((x1,y1))
                
        return min_area if min_area != math.inf else 0
        
        