def findThreeLargestNumbers(array):
    res = [None,None,None]
	
	for num in array:
		largerThree(num,res)
		
	return res

def largerThree(num,res):
	if  res[2] == None or num > res[2]:
		swap(num,2,res)
		
	elif res[1] == None or num > res[1]:
		swap(num,1,res)
	
	elif res[0] == None or num > res[0]:
		swap(num,0,res)

def swap(num,idx,res):
	for i in range(idx+1):
		if i == idx:
			res[idx] = num
		else:
			res[i] = res[i+1]	