# Time = O(2^n)
# Space = O(n)

# N starting from 1
def getNthFib(n):
    # Write your code here.
    if n == 2:
		return 1
	elif n == 1:
		return 0
	return getNthFib(n-1) + getNthFib(n-2)