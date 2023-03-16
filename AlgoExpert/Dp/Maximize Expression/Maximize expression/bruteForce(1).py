# Time = O(n^4)
# space = O(1)

import math
def maximizeExpression(array):
    if len(array) < 4:
		return 0
	
	max_Expression = -math.inf
	for a in range(len(array)-3):
		aValue = array[a]
		for b in range(a+1, len(array) - 2):
			bValue = array[b]
			for c in range(b+1, len(array) - 1):
				cValue = array[c]
				for d in range(c+1, len(array)):
					dValue = array[d]
					ExpressionVal = (aValue - bValue + cValue - dValue)
					max_Expression = max(max_Expression , ExpressionVal)
					
	return max_Expression
