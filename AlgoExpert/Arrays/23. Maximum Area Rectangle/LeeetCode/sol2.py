# time = O(n^2)
# space = O(n)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = self.generatePoint(points)
        minArea = float("inf")
        
        for cur_idx , p2 in enumerate(points):
            p2x , p2y = p2
            
            for prev_idx in range(cur_idx):
                p1x , p1y = points[prev_idx]
                
                # if the point are horizontal and vertical then they will not form diagonal
                if p1x == p2x or p1y == p2y:
                    continue
                    
                diagonalOne = False
                if self.convert_point(p1x, p2y) in point_set:
                    diagonalOne = True
                    
                diagonalTwo = False
                if self.convert_point(p2x, p1y) in point_set:
                    diagonalTwo = True
                    
                if diagonalOne and diagonalTwo:
                    cur_sum = abs(p2x - p1x) * abs(p2y - p1y)
                    minArea = min(minArea , cur_sum)
                    
        return minArea if minArea != float("inf") else 0
        
    def generatePoint(self, points):
        point_set = set()
        
        for point in points:
            x, y = point
            
            point_string = self.convert_point(x,y)
            
            point_set.add(point_string)
        
        return point_set
    
    
    def convert_point(self , x, y):
        return str(x) + ":" + str(y)