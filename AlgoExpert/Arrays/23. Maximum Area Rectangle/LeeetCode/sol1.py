# Time = O(n^2)
# Space = O(n)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        y_axis_point_that_lie_on_same_x_axis_point = self.getPoints(points)
        
        sorted_x_axis_points  = sorted(y_axis_point_that_lie_on_same_x_axis_point.keys())
        
        minArea = float("inf")
        
        y_axis_points_that_share_common_x_axis = {}
        
        
        for x in sorted_x_axis_points:
            y_axis_points = y_axis_point_that_lie_on_same_x_axis_point[x]
            
            y_axis_points.sort()
            
            for cur_idx , p2 in enumerate(y_axis_points):
                for prev_idx in range(cur_idx):
                    p1 = y_axis_points[prev_idx]
                    
                    
                    y_axis_point_key = str(p1) + ":" + str(p2)
                    
                    
                    if y_axis_point_key in y_axis_points_that_share_common_x_axis:
                        cur_area = (x - y_axis_points_that_share_common_x_axis[y_axis_point_key]) * (p2 - p1)
                        minArea = min(minArea , cur_area)
                    
                    y_axis_points_that_share_common_x_axis[y_axis_point_key] = x
                    
                               
        return minArea if minArea != float("inf") else 0
        
    def getPoints(self, points):
        common_points_on_x_axis = {}
        
        for point in points:
            x, y = point
            
            if x not in common_points_on_x_axis:
                common_points_on_x_axis[x] = []
            
            common_points_on_x_axis[x].append(y)
            
        return common_points_on_x_axis