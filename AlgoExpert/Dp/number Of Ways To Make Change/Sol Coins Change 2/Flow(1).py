'''
# https://leetcode.com/problems/coin-change-ii/discuss/3138946/Brute-Force-to-Optimal-or-Python-Solution

# Flow from brute force to Optimal solution
    --> First Backtracking
    --> Then Recursion
    --> Then memoization
    --> Then dp solution
    --> Then 1D dp solution

# Some hints to remember

Hint:
When the question says - "Give Number of ways" or "Return the number of combinations", 
We actual need to return all the possible ways -- So the best way to do this is by "Trying out all the combinations"

And to try out all the combination we use -- "Recursion"

Hint:
When we can use input value for "Infinite times" or "Any number of times".
    * We simple have to consider the current value and find target, and 
    * Not include the current value and find target.

We can express Recursion with 3 steps:
    1. Since input is in array format - "We can express in terms of index".
    2. Explore all the possibilites . ie,.
        a. Include the current index value.
        b. Do not include the current index value.
    3. Sum all the possibilities.

eg: It would look somehthing like
    sum of all ways = F(sum including the current index) + F(sum with out the current index)

Logic of Target:
    1. If we do not inclulde the current value - then our target value would not change.
    2. If we include the current value:
        Our target value will reduce to a new value
        "Note:  if target value < current value : then we cannot include current value"


Base Case Logic:
    We always return a 0 or 1, when we are trying to find number of ways to reach target.
    1. Return 1 -  if we are able to reach target
    2. Return 0 - If we could not reach target.
    * this happens when
        # Index go out of bound before reaching the target.
        # Our new target will cross the target amount (if top down), or new target will be less than 0 (if bottom up)
        
        

'''