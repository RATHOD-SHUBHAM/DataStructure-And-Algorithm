# Time = O(n^2)
# Space = O(n)

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_no_points_on_line = 1
        
        for i , p1 in enumerate(points):
            slopes = {}
            
            for idx in range(i + 1, len(points)):
                p2 = points[idx]
                
                y, x = self.getSlopes(p1, p2)
                
                slopesKey = self.generateKey(y, x)
                
                if slopesKey not in slopes:
                    slopes[slopesKey] = 1
                    
                slopes[slopesKey] += 1
                
            max_no_points_on_line = max(max_no_points_on_line , max(slopes.values() , default = 0) )
        
        return max_no_points_on_line
    
    def getSlopes(self, p1, p2):
        p1x, p1y = p1
        p2x, p2y = p2
        
        slope = [1,0]
        
        if p1x != p2x:
            yVal = p2y - p1y
            xVal = p2x - p1x
            
            gcd = self.GCD(abs(xVal) , abs(yVal))
            
            yVal = yVal // gcd
            xVal = xVal // gcd
            
            if xVal < 0:
                xVal *= -1
                yVal *= -1
                
            slope = [yVal, xVal]
        
        return slope
    
    def GCD(self, a , b):
        while True:
            if a == 0:
                return b
            if b == 0:
                return a
            a , b = b , a%b
    
    def generateKey(self, y, x):
        return str(y) + ":" + str(x)