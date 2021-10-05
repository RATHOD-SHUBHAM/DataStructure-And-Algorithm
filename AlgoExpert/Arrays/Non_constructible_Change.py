# if you are stuck in a problem 
# try sorting it first and then implement the logic

# if we ever get a coin , that is greater than than the amount of current change + 1
# that means we cannot make amount of previous change + 1 
def nonConstructibleChange(coins):
    coins.sort() # time complexity = O(nlogn)
	
	change = 0
	
	for coin in coins:
		if coin > change+1:
			return change+1
		change += coin
		
	return change+1
