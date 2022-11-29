# Time = O(n^2)
# Space = O(n)

# if there are same y cordinates on different x axis then we can form a rectangle

def minimumAreaRectangle(points):
    # get all the points on x axis
	points_on_x_axis = getPoints(points)
	print("points_on_x_axis", points_on_x_axis)

	minArea = float("inf")

	# dictionary to store the x axis for the common y axis
	# store the latest x_axis. As we will be moving from left to right.
	# the latest will be the smallest
	x_axis_with_common_point = {}

	# move from left to right - this will give us the min area
	sortedPoints = sorted(points_on_x_axis.keys())
	print("sortedPoints key: ",sortedPoints)


	# for every point on x axis. get the y axis value
	for x in sortedPoints:
	# get the y coordinates
	y_coordinates = points_on_x_axis[x]
	print("y_coordinates : ",y_coordinates)

	# sort the y coordinates. - move from down to top
	# because we want to compare same up and down value

	y_coordinates.sort()
	print("y_coordinates sort : ",y_coordinates)

	# go over each y_value and combine with the previous y_value 
	# and check if the same y_value alredy exist
	for cur_idx, y2 in enumerate(y_coordinates):
		print("cur_idx: ",cur_idx)
		print("y2: ",y2)
		
		for prev_idx in range(cur_idx):
			print("prev_idx: ",prev_idx)
			y1 = y_coordinates[prev_idx]
			
			# convert it from 2,5 to 2:5
			point_on_y_axis = str(y1) + ":" + str(y2)
			print("point_on_y_axis: ",point_on_y_axis)
			
			# check if this point is present on some other x axis as well
			if point_on_y_axis in x_axis_with_common_point:
				cur_area = (x - x_axis_with_common_point[point_on_y_axis]) * (y2 - y1)
				minArea = min(minArea, cur_area)
				print("minArea : ",minArea)
			
			# update the dictionary
			x_axis_with_common_point[point_on_y_axis] = x
			print("x_axis_with_common_point : ",x_axis_with_common_point)
			print("\n")
		print("\n")
				
	return minArea if minArea != float("inf") else 0

def getPoints(points):
	point_on_x_axis = {}
	
	for point in points:
		x, y = point
		
		if x not in point_on_x_axis:
			point_on_x_axis[x] = []
		
		point_on_x_axis[x].append(y)
	
	return point_on_x_axis
