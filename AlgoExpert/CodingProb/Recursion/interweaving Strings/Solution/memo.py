# Tc: O(one + two) , Sc:O(one + two)

def interweavingStrings(one, two, three):
    # base case
    if len(three) != len(one) + len(two):
        return False

    # len + 1 because we will also compare when index moves out of range eg: aaa_
    memo = [[None for _ in range(len(two) + 1)] for _ in range(len(one) + 1)]

    i = 0
    j = 0

    return backtrack(i , j, one, two, three, memo)

def backtrack(i , j, one, two, three, memo):
    # if value here already compared
    if memo[i][j] is not None:
        return memo[i][j]

        
    k = i + j
    
    # base case: when k moves out of string three. it has sucessfully completed all comparison
    if k == len(three):
        return True

    # check the current value with i
    if i < len(one) and one[i] == three[k]:
        # save the comparision to cache.
        # move to the next value of i.
        memo[i][j] = backtrack(i + 1 , j, one, two, three, memo)

        # if all the next comparison return true
        if memo[i][j] == True:
            return True

    # if i is false then check with j value
    if j < len(two) and two[j] == three[k]:
        memo[i][j] = backtrack(i, j+1, one, two, three, memo)

        if memo[i][j]:
            return True

    
    # if the both the value dont match - make the current value in memo as false
    memo[i][j] = False
    # if both the value dont match, return false
    return False
            
    
