# time and space = O(n^2)
def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    if len(arrayOne) != len(arrayTwo):
		return False
	# base case
	if len(arrayOne) == 0 and len(arrayTwo) == 0:
		return True
	
	if arrayOne[0] != arrayTwo[0]:
		return False
	
	leftSubtree_One = getsmaller(arrayOne)
	leftSubtree_Two = getsmaller(arrayTwo)
	rightSubtree_One = getlarger_or_equal(arrayOne)
	rightSubtree_Two = getlarger_or_equal(arrayTwo)
	
	return sameBsts(leftSubtree_One, leftSubtree_Two) and sameBsts(rightSubtree_One, rightSubtree_Two)

def getsmaller(array):
	smaller = []
	for i in range(1,len(array)):
		if array[i] < array[0]:
			smaller.append(array[i])
	return smaller

def getlarger_or_equal(array):
	larger_or_equal = []
	for i in range(1,len(array)):
		if array[i] >= array[0]:
			larger_or_equal.append(array[i])
	return larger_or_equal