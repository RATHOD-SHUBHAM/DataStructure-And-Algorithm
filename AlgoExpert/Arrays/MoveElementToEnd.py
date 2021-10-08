# Time Complexity = O(n) | Space = O(1)
def moveElementToEnd(array, toMove):
	i = 0
	j = len(array) - 1
	
	while i < j: # make sure they dont cross each other
		while i < j and array[j] == toMove: # so that j doesnt cross i when swapping happens
			j -= 1
		if array[i] == toMove:
			array[i], array[j] = array[j], array[i] # swap elements
			
		i += 1

		
	return array
