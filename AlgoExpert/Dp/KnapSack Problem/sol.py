# Time and space = O(nc)
# n is number of item and c is capacity
def knapsackProblem(items, capacity):
	valueTable = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]
	# print(valueTable)
	
	# fill in table using formula
	for i in range(1, len(items)+1):
		value = items[i-1][0] # added extra column in front and left for my table
		# so for items it will one value behind
		
		weight = items[i-1][1]
		
		for j in range(capacity + 1):
			if weight > j:
				valueTable[i][j] = valueTable[i-1][j]
			else:
				valueTable[i][j] = max(
					valueTable[i-1][j] , valueTable[i-1][j-weight] + value
				)
	
	# return max value and index of items that caused max value
	print(valueTable)
	return [valueTable[-1][-1], knapsack_item(valueTable, items)]

def knapsack_item(valueTable, items):
	seq = []
	
	i = len(valueTable) - 1
	j = len(valueTable[0]) - 1
	
	while i > 0:
		if valueTable[i][j] == valueTable[i-1][j]:
			i -= 1
		else:
			seq.append(i-1)
			j = j - items[i-1][1] # col - weight
			i -= 1 # decrement col
			
		if j == 0:
			break
	return list(reversed(seq))
			