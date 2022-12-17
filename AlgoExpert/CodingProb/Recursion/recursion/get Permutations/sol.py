'''
+ = creates a new array
append = modifies the existing array

'''

# time = Space = O(n * n!)
def getPermutations(array):
	if not array:
		return array
    permutation = []
	curPermutation = []
	# permutation will be the same list that will be passed
	# curPermutation = is a new array that is passed all time
	helper(array,curPermutation,permutation)
	return permutation

def helper(array, curPermutation,permutation):
	if array == []: # check the base case
		permutation.append(curPermutation) # modify the original list
	else:
		for i in range(len(array)):
			newPermutation = curPermutation + [array[i]] # create a new list and Doesnot modify the original list
			newArray = array[ : i] + array[i+1 : ]
			helper(newArray,newPermutation,permutation)
