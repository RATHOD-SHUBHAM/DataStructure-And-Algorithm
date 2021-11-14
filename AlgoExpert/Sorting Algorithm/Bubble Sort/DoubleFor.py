# Time Complexity = O(n^2)
# Space Complexity = O(1)

def bubbleSort(array):
    n = len(array) - 1

	for i in range(n):
		for j in range(n-i):
			if array[j] > array[j+1]:
				array[j],array[j+1] = array[j+1],array[j]

	return array
