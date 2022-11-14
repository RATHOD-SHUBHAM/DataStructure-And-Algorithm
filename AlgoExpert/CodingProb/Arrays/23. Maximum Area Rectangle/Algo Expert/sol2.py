# Time = O(n^2)
# Space = O(n)

# here if there are same y cordinates on different x axis then we can form a rectangle

def minimumAreaRectangle(points):
    # get all the points on x axis
	points_on_x_axis = getPoints(points)
	print(points_on_x_axis)
	
	minArea = float("inf")
	
	x_axis_with_common_point = {}
	
	# move from left to right
	sortedPoints = sorted(points_on_x_axis.keys())
	print(sortedPoints)
	
	
	for x in sortedPoints:
		# get the y coordinates
		y_coordinates = points_on_x_axis[x]
		
		# sort the y coordinates. because we want to compare same up and down value
		y_coordinates.sort()
		
		for cur_idx, y2 in enumerate(y_coordinates):
			for prev_idx in range(cur_idx):
				y1 = y_coordinates[prev_idx]
				
				# convert it from 2,5 to 2:5
				point_on_y_axis = str(y1) + ":" + str(y2)
				
				# check if this point is present on some other x axis as well
				if point_on_y_axis in x_axis_with_common_point:
					cur_area = (x - x_axis_with_common_point[point_on_y_axis]) * (y2 - y1)
					minArea = min(minArea, cur_area)
				
				
				x_axis_with_common_point[point_on_y_axis] = x
				
	return minArea if minArea != float("inf") else 0

def getPoints(points):
	point_on_x_axis = {}
	
	for point in points:
		x, y = point
		
		if x not in point_on_x_axis:
			point_on_x_axis[x] = []
		
		point_on_x_axis[x].append(y)
	
	return point_on_x_axis
