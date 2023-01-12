# same straight line = slope = y = mx+c
# points = y2 - y1 / x2 - x1
# find the max points
# for each point i can see how many other point lie on the same slope
# get the max and store it somewhere
# repeat it for the rest of my points

# to check if the line lie on the same slope -- {slope : no of points}

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_points_on_line = 1 # by default we will have atleast one point for a slope
        
        for idx1 , p1 in enumerate(points):
            # get the slope value for this point
            slope = {}
            
            # compute the slope with the rest of points
            for idx2 in range(idx1 + 1, len(points)):
                p2 = points[idx2]
                
                # compute slope for 2 points
                rise , run = self.getSlope(p1, p2)
                
                # once i have the slope , add the slope to dict
                # if the slope already exists - increase the no of points
                
                # generate the hashKey
                hashKey = self.getHashkey(rise, run)
                
                if hashKey not in slope:
                    slope[hashKey] = 1
                    
                slope[hashKey] += 1
                
            # get the maximum value from current slopes and compare with exising max_value
            max_points_on_line = max(max_points_on_line , max(slope.values() , default = 0))
        
        return max_points_on_line
    
    def getSlope(self, p1 , p2):
        p1x , p1y = p1
        p2x , p2y = p2
        
        slope = [1 , 0] # vertical slope
        # horizontal slope = 0
        
        if p1x != p2x:
            
            xDiff = p2x - p1x
            yDiff = p2y - p1y

            # we cant have flaot value as the key in dict
            gcd = self.GCD(abs(xDiff) , abs(yDiff))

            xDiff = xDiff // gcd
            yDiff = yDiff // gcd

            # let not have negative value in denominator
            if xDiff < 0:
                xDiff *= -1
                yDiff *= -1

            slope = [yDiff, xDiff]
            
        return slope
    
    def GCD(self, a , b):
        if a == 0:
            return b
        return self.GCD( b % a , a)
        
    
    def getHashkey(self, numerator, denominator):
        return str(numerator) + ":" + str(denominator)