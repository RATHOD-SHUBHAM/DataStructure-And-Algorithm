def getNthFib(n, memoize = {1:0,2:1}):
    # Write your code here.
    if n in memoize:
		return memoize[n]
	else:
		memoize[n] = getNthFib(n-1) + getNthFib(n-2)
		return memoize[n]