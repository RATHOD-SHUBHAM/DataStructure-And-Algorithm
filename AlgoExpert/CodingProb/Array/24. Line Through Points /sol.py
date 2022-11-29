def lineThroughPoints(points):
    max_points_on_the_line = 1
	
    for idx, p1 in enumerate(points):
        print("point p1 is: ",p1)
        # get the slope for each point
        slopes = {}
        
        for idx2 in range(idx + 1, len(points)):
            p2 = points[idx2]
            print("point p2 is: ",p2)

            # calculate the slope between these 2 points
            rise, run = getSlope(p1, p2)
            print("rise: ",rise)
            print("run: ",run)
            
            # add the slope to hash map
            slopeKey = addToHash(rise,run)
            print("slopeKey: ",slopeKey)

            # slope value indicate the number of point that share a common slope
            if slopeKey not in slopes:
                slopes[slopeKey] = 1
                
            slopes[slopeKey] += 1
            print("slopes: ",slopes)
        
        max_points_on_the_line = max(max_points_on_the_line , max(slopes.values(), default = 0))
        print("max_points_on_the_line : ",max_points_on_the_line)
        
        print("\n")
        print("---------------------------------------")
        print("\n")
        
        
    print("\n===============================================")		
    return 	max_points_on_the_line
			
			
def getSlope(p1, p2):
	p1x , p1y = p1
	p2x, p2y = p2
	print("\n")
	print("p1x, p1y : ",p1x,p1y)
	print("p2x, p2y : ",p2x, p2y)
	
	slope = [1,0] # vertical slope
    # horizontal line slope will be zero -> x1 = x2
	
	if p1x != p2x:
		yDiff = p2y - p1y
		print("yDiff: ",yDiff)
		xDiff = p2x - p1x
		print("xDiff: ",xDiff)
		
		gcd = greatestCommonFactor(abs(xDiff), abs(yDiff))
		print("gcd: ",gcd)
		
		
		# compute the gcd to sove floating point error,
		yDiff = yDiff // gcd
		print("yDiff: ",yDiff)
		xDiff = xDiff // gcd
		print("xDiff: ",xDiff)
		
		# if denominator has negative represent it as -y/x rather than y/-x
		if xDiff < 0:
			xDiff *= -1
			yDiff *= -1
			
		slope = [yDiff, xDiff] # rise, run
		print("slope: ",slope)
		print("\n")
		
	return slope
		
	
def greatestCommonFactor(a, b): 
    if a == 0:
        return b
    return greatestCommonFactor(b % a , a)


def addToHash(numerator, denominator):
	return str(numerator) + ":" + str(denominator)