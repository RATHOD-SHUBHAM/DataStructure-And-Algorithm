# Time Complexity = O(n^2)
# Space Complexity = O(1)

def bubbleSort(array):
    n = len(array) - 1
	helper(array,n)
	return array

def helper(array,n):
	for i in range(n):
		for j in range(n-i):
			if array[j] > array[j+1]:
				swap(array,j,j+1)
				
def swap(array,left,right):
	array[left],array[right] = array[right],array[left]
