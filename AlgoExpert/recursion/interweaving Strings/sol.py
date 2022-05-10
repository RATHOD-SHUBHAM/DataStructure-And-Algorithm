# Time = space = O(nm) where n is length of one and m is length of two

def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
		return False
	
	return areInterwoven(one,two,three,0,0)

def areInterwoven(one,two,three,i,j):
	print("i is : ",i)
	print("j is : ",j)
	
	k = i + j
	print("k is : ",k)
	
	if k == len(three):
		return True
	
	if i < len(one) and one[i] == three[k]:
		print("i is : ",i)
		print("j is : ",j)
		print("k is : ",k)
		print("one[i] : ",one[i])
		print("three[k] : ",three[k])
		print("\n")
		if areInterwoven(one,two,three,i+1,j):
			return True
	
	if j < len(two) and two[j] == three[k]:
		print("i is : ",i)
		print("two[j] : ",two[j])
		print("k is : ",k)
		print("three[k] : ",three[k])
		print("\n")
		return areInterwoven(one,two,three,i,j+1)
	
	print("returning False")
	return False