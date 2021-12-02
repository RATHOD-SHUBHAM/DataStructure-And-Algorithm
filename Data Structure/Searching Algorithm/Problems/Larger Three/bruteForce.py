# Time Complexity : O(n)
# Space Complexity : O(1) --> becasue I am using extra space which is smaller than len(array)

def findThreeLargestNumbers(array):
    res = [None,None,None]
	
	for num in array:
		largerThree(num,res)
		
	return res

def largerThree(num,res):
	if  res[2] == None or num > res[2]:
		res[0] = res[1]
		res[1] = res[2]
		res[2] = num
		
	elif res[1] == None or num > res[1]:
		res[0] = res[1]
		res[1] = num
	
	elif res[0] == None or num > res[0]:
		res[0] = num
