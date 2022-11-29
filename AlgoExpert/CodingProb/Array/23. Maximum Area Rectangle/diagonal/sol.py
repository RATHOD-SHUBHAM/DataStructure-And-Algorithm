# Time = O(n^2)
# Space = O(n)

# Catch here is to recognize
# we check for the opposite diagonal point
# For example, 
# if the points are (1, 5) and (7, 8), 
# we check if we also have (1, 8) and (7, 5). 
# If we do, we have a candidate rectangle.

def minimumAreaRectangle(points):
	# add the points in a set: ip array wont have duplicate
	points_set = createSet(points)
    print("points_set: ",points_set)

	minArea = float("inf")

    # go through each points
	for cur_idx, p2 in enumerate(points):
		# [1,5]
		p2x , p2y = p2
        print("curIdx: ",cur_idx)
        print("p2x : ", p2x)
        print("p2y : ", p2y)

        # grab all the previous point
		for prev_idx in range(cur_idx):
			#[1,5], [5,1]
			p1x, p1y = points[prev_idx]
            print("prev_idx: ",prev_idx)
            print("p1x : ", p1x)
            print("p1y : ", p1y)
			
			# check if they share same x or y axis
			# if so then diagonal cannot form
			sharePoint = p1x == p2x or p2y == p1y
			
			if sharePoint:
				continue
			# check if the diagonal values exist
                
			# diagonals: (p1x, p2y) , (p2x, p1y)
			diagonalOne = convert(p1x, p2y)
            print("diagonalOne : ",diagonalOne)
			
			diagonalOneExist = False
			if diagonalOne in points_set:
				diagonalOneExist = True
				
			diagonalTwo = convert(p2x, p1y)
            print("diagonalTwo : ",diagonalTwo)
			
			diagonalTwoExist = False
			if diagonalTwo in points_set:
				diagonalTwoExist = True

            # check if both the diagonal value exist
			oppositeDiagonalExist = False
			if diagonalTwoExist and diagonalOneExist:
				oppositeDiagonalExist = True

            
			if oppositeDiagonalExist:
				# calculate the area: eg [1,5] [ 1,2] [2,2] [2,5]
                # area = width * height
				cur_area = abs(p1x - p2x) * abs(p1y - p2y)
				minArea = min(minArea, cur_area)
				
	return 0 if minArea == float("inf") else minArea
	
def createSet(points):
	point_set = set()
	
	for point in points:
		# [1,5] : convert it into 1:5 format
		x , y = point
		pointString = convert(x,y)
		point_set.add(pointString)
	
	return point_set

def convert(x,y):
	return str(x) + ":" + str(y)
		