# Time and space = O(n)
def arrayOfProducts(array):
	total_prod = [1] * len(array)
	left_prod = [1] * len(array)
	right_prod = [1] * len(array)
	
	cur_left_prod = 1
	for i in range(len(array)):
		# add the product until this index
		left_prod[i] = cur_left_prod
		# now include this value so that it gets added in next index
		cur_left_prod *= array[i]
		
	cur_right_prod = 1
	for i in reversed(range(len(array))):
		right_prod[i] = cur_right_prod
		cur_right_prod *= array[i]
		
	for i in range(len(array)):
		total_prod[i] = left_prod[i] * right_prod[i]
		
	return total_prod