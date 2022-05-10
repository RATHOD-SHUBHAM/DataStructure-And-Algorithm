# time complexity = o(n)
# space complexity = o(n)

def twoNumberSum(array, targetSum):

	if not array or len(array) == 1:
		return []
    # Write your code here.
	dicti = {}
	
	for i in range(len(array)):
		diff = targetSum - array[i] # calculate diff between target and every other item in the array
		
		if diff in dicti:
			return ([diff, array[i]])
		
		else:
			dicti[array[i]] = diff
			
	return [] # if the array has no element or just one element or if there was no pair then return the empty list