# Time Complexity = O(n^2)
# Space Complexity = O(1)

def selectionSort(array):
    for i in range(len(array)):
		min_val = array[i]
		
		for j in range(i,len(array)):
			if array[j] < min_val:
				min_val = array[j]
				swap(array,i,j)
						
	return array

def swap(array,i,j):
	array[j], array[i] = array[i], array[j]
