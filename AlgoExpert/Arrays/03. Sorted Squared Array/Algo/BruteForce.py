def sortedSquaredArray(array):
	# todo: Brute force method
	
	# because we are using a seperate array. our space complexity is O(n)
	result = []
	
	if not array:return result
	
	for num in array:
		res = num * num
		result.append(res)
		
	# because ill use sort(). Our run time will become O(nlogn)
    # we need to sort because - 7 * -7 will be 49
	result.sort()
	return result


    # hint :  when the input is osrted in ascending order. There are high chances that we could solve the problem in linear time