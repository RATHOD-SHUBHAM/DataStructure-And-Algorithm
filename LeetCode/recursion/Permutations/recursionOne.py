def getPermutations(array):
	if not array:
		return array
    permutation = []
	# permutation will be the same list that will be passed
	# [] = is a new array that is passed all time
	helper(array,[],permutation)
	return permutation

def helper(array, curPermutation,permutation):
	if array == []: # check the base case
		permutation.append(curPermutation) # modify the original list
	else:
		for i in range(len(array)):
			newPermutation = curPermutation + [array[i]] # create a new list and Doesnot modify the original list
			newArray = array[ : i] + array[i+1 : ]
			helper(newArray,newPermutation,permutation)
