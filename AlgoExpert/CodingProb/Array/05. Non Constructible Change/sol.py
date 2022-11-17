# if you are stuck in a problem 
# try sorting it first and then implement the logic

# if we ever get a coin , that is greater than than the amount of current change + 1
# that means we cannot make amount of previous change + 1 

def nonConstructibleChange(coins):
	# O(nlogn)
    coins.sort() # inplace sorting
	change = 0
	#O(n)
	for coin in coins:
		#O(1)
		if coin > change+1:
			return change+1
		change += coin
	# this is the change we cannot create
	return change+1
# runtime = O(nlogn) space O(1)