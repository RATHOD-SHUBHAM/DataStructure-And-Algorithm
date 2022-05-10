# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.

# Time = O(n)
# Space = O(n)

def productSum(array, multiplier = 1):
    # Write your code here.
    sum = 0
	
	for i in array:
		if type(i) is list:
			sum += productSum(i, multiplier + 1)
		else:
			sum += i
			
	return sum * multiplier