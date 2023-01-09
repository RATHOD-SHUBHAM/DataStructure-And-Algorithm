# Time = O(n^2)
# Space = O(n)

# horizontal line : slop will be 0 
'''
		rise	y2 - y1
slope = ---- =  -------
		 run	x2 - x1

'''
""" 
to avoid the precision issue with the float/double number,
using a pair of co-prime numbers to represent the slope.
"""
def lineThroughPoints(points):
    max_points_on_the_line = 1
	
	for idx, p1 in enumerate(points):
		print("point p1 is: ",p1)
		slopes = {}
		
		for idx2 in range(idx + 1, len(points)):
			p2 = points[idx2]
			print("point p2 is: ",p2)
			
			rise, run = getSlope(p1, p2)
			print("rise: ",rise)
			print("run: ",run)
			
			# add the slope to hash map
			slopeKey = addToHash(rise,run)
			
			print("slopeKey: ",slopeKey)
			
			if slopeKey not in slopes:
				slopes[slopeKey] = 1
				
			slopes[slopeKey] += 1
			print("slopes: ",slopes)
		
		# get the maximum value from current slopes and compare with exising max_value
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
	while True:
		if a == 0:
			return b
		if b == 0:
			return a
		'a , b = b , a % b'
		x = a
		a = b
		b = x % b


def addToHash(numerator, denominator):
	return str(numerator) + ":" + str(denominator)
	