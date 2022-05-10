# Time = O(low * high * n)
# Space = O(low * high)

def ambiguousMeasurements(measuringCups, low, high):
    # Write your code here.
    return canMeasure(measuringCups, low, high,{})

def canMeasure(measuringCups, low, high,memoize):
	key = createKey(low,high) #{"low:high" : "True/False"}
	
	# check if the value is present in dict
	if key in memoize:
		return memoize[key]
	
	# base case
	if low <= 0 and high <=0:
		return False
	
	can_Measure = False
	for cup in measuringCups:
		cupLow, cupHigh = cup
		
		if low <= cupLow and cupHigh <= high:
			can_Measure = True
			break # go out of for loop
		
		# print("newLow : ",low-cupLow)
		# print("newHigh : ",high-cupHigh)
		# print("\n")
		can_Measure = canMeasure(measuringCups, low-cupLow , high-cupHigh, memoize)
		if can_Measure:
			break # when can measure from recursive call return True break out of for loop
	
	memoize[key] = can_Measure
	return can_Measure


def createKey(low,high):
	return str(low)+":"+str(high)