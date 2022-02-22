# Time = O(nlogn + n + m^2)
# space = O(nm)
# m = len of longest string
# n = number of ele in string

def longestStringChain(strings):
    # sort the string
	strings = sorted(strings, key = len) #O(nlogn)
	
	# append to dictionary
	cache = {}
	for string in strings:
		cache[string] = {
			"nextString" : "",
			"maxChainLen" : 1
		}
	
	# break the string and check if it is present in strings list
	for string in strings:
		findLongestChain(string, cache)
	
	# print(cache)
		
	return buildMaxChain(strings,cache)
# O(m^2)
def findLongestChain(string, cache):
	for i in range(len(string)):
		smaller_string = getSmallerString(i,string)
		
		if smaller_string not in cache:
			continue
		
		updateCache(string, cache, smaller_string)
		
def getSmallerString(i, string):
	return string[ :i] + string[i+1 : ] # O(n)

def updateCache(string, cache, smaller_string):
	smaller_string_chain_len = cache[smaller_string]["maxChainLen"]
	cur_string_chain_len = cache[string]["maxChainLen"]
	
	if smaller_string_chain_len + 1 > cur_string_chain_len:
		cache[string]["maxChainLen"] = smaller_string_chain_len + 1
		cache[string]["nextString"] = smaller_string
		

def buildMaxChain(strings,cache):
	# find the element with maxChain len
	len_of_maxChain = 0
	max_len_stringName = ""
	
	for string in strings:
		if cache[string]["maxChainLen"] > len_of_maxChain:
			len_of_maxChain = cache[string]["maxChainLen"]
			max_len_stringName = string
			
	# print(max_len_stringName)
	
	result = []
	curString = max_len_stringName
	
	while curString != "":
		result.append(curString)
		curString = cache[curString]["nextString"]
		
	return [] if len(result) == 1 else result