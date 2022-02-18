# Time and space= O(n)

import math
def maximizeExpression(array):
	if len(array) < 4:
		return 0
	
    maxA = [array[0]] * len(array)
	maxA_minus_B = [-math.inf] * len(array)
	maxA_minus_B_plus_C = [-math.inf] * len(array)
	maxA_minus_B_plus_C_minus_D = [-math.inf] * len(array)
	
	for i in range(1, len(array)):
		maxA[i] = max(maxA[i-1] , array[i])
	print(maxA)
	
	# since i cant inclue a , ill start from index 1
	for i in range(1,len(array)):
		maxA_minus_B[i] = max(maxA_minus_B[i-1], maxA[i-1]- array[i])
	print(maxA_minus_B)
	
	for i in range(2, len(array)):
		maxA_minus_B_plus_C[i] = max(maxA_minus_B_plus_C[i-1], maxA_minus_B[i-1] + array[i])
	print(maxA_minus_B_plus_C)
	
	for i in range(3, len(array)):
		maxA_minus_B_plus_C_minus_D[i] = max(maxA_minus_B_plus_C_minus_D[i-1], maxA_minus_B_plus_C[i-1] - array[i])
	print(maxA_minus_B_plus_C_minus_D)
	
	return maxA_minus_B_plus_C_minus_D[-1]