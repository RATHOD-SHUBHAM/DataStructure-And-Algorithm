# Time = O(n^2)
# Space = O(n)
def rightSmallerThan(array):
    smallest = []
	for i in range(len(array)):
		count = 0
		for j in range(i+1,len(array)):
			if array[j] < array[i]:
				count += 1
		smallest.append(count)
	return smallest