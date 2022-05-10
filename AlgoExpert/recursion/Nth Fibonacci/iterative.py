# Time = O(n)
# Space = O(1)

def getNthFib(n):
    # Write your code here.
	
	if n == 1:
		return 0
	elif n == 2:
		return 1
    curSum = 0
	prev = 1
	pprev = 0
	
	for i in range(2,n):
		curSum = prev + pprev
		pprev = prev
		prev = curSum
		
	return curSum