# Time and Space = O(nd) | O(n)

'''
Assumption:
use can make 0$ by not spending anything.

Calculate
eg1
Can we use 1$ to make 0$ - no.
Can we use 1$ to make 2$ - yes. --. 1 + 1 $ = 2$
eg2
can we use 2$ to make 10$ - yes -- 2 + 2 + 2 + 2 + 2 = 10$
but we cant make a 10$ with 2$

Equation:
can you make x$ from y$
eg can you make 2$ from 1$
if y <= x:
	2$ = 1 + 1

assume
# x is target and y is coin	
if y <= x:
	x = [x] + [x-y]
	
	# eg - no of ways of making 3$ from 1 2 and 3 dollar
	# initaially - no of making3$ from each is 0
	0  1 2 3
	[1,0,0,0]
	3$ = 3*1 # [0] + [1-0] 
	[1,1,1,1] # no of ways of making 1 2 3 from 0 $
	3$ = 2*1 + 1*1 # [1] + [1-1]
	[1,1,1,0] # no of ways of making 2 from 0 and 1 $
	3$ = 1*1*1 # [1] + [1-1]
	[1,1,1,3] # no of ways of making 3 form 0 1 2 $
	

'''

def numberOfWaysToMakeChange(n, denoms):
    ways = [0] * (n+1)
	
	# Assumption: assume we can make 0$ by not spending anything.
	ways[0] = 1
	
	# y = denoms
	# x = n = target
	# calculate no of ways to make x from y
	for y in denoms:
		for x in range(n+1):
			'''
			can you make x$ from y$
			eg 
				can you make 2$ from 1$ - yes
				can you make 1$ from 2$ -- no
			'''
			if y <= x:
				ways[x] = ways[x] + ways[x-y]
				print("x is ",x)
				print("y is : ",y)
				print("ways to create change ", ways)
				
	return ways[-1]
