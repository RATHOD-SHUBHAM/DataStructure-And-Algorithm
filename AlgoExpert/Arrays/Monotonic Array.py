def isMonotonic(array):
    increasing = True
	decreasing = True
	
	
	for i in range(1, len(array)):
		if array[i] < array[i-1]:
			increasing = False
		if array[i] > array[i-1]:
			decreasing = False	
			
	return increasing or decreasing