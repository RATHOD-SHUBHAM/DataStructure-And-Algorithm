# Keep appending the minimun element to the front
def selectionSort(array):
    # Write your code here.
	for i in range(len(array)):
		min_val = array[i]
		for j in range(i,len(array)):
			if array[j] < min_val:
				min_val = array[j]
				array[i], array[j] = array[j], array[i]		
	return array
