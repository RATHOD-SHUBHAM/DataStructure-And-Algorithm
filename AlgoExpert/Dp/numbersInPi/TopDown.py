# Top down approach
'''
Time = O(n^3 + m)
n^2 because we go through every element in array and then its corresponding subarray
n = Slicing each element
so O(n^3)

m = number table

so totally = O(n^3 + m)


Space = O(n + m)
# n = cache
# m = number table
'''
import math
def numbersInPi(pi, numbers):
    # convert list of number to dictionary : O(n)
	numberTable = {number: True for number in numbers}
	print(numberTable)
	
	idx = 0
	cache = {} # to store number of spaces
	minSpace = getMinSpace(pi, numberTable, cache , idx)
	
	return -1 if minSpace == math.inf else minSpace

def getMinSpace(pi, numberTable, cache , idx):
	if idx == len(pi):
		return -1
	
	if idx in cache:
		return cache[idx]
	
	minSpace= math.inf
	
	print("idx: ",idx)
	for i in range(idx,len(pi)):
		print("i: ",i)
		
		prefix = pi[idx : i+1] # O(n) time
		print("prefix: ",prefix)
		
		if prefix in numberTable:
			# calculate min spaces for subarray
			print("passing i+1 : ",i+1)
			minSpace_subarry = getMinSpace(pi, numberTable, cache , i+1)
			print("prefix: ",prefix)
			print("minSpace_subarry : ",minSpace_subarry)
			
			# get the minimum space
			minSpace = min(minSpace, minSpace_subarry + 1)
			print("minSpace: ",minSpace)
			
	cache[idx] = minSpace
	print("cache: ",cache)
	print("\n")
	
	return cache[idx]