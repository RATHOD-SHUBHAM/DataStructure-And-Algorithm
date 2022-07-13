'''

473. Matchsticks to Square

You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

 

Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
 

Constraints:

1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 108


'''

# Trying doing on pen and paper for
# [1,1,1,1,1,2,2] and [1,1,2,4]



# Time: O(4^n)
# Space: O(n)

class Solution: 
    def makesquare(self, matchsticks: List[int]) -> bool:
        # get to know the lenght of side of square
        side_len = sum(matchsticks) // 4
        
        
        # Check if we can form a square
        if side_len != sum(matchsticks) / 4:
            return False
        
        matchsticks.sort(reverse = True)
        
        # keep track of the each sides
        sides = [0] * 4
        
        def backtracking(idx):
            # base case
            if idx == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3] == side_len
            
            # Filling in the 4 sides
            for i in range(4):
                # check if the side len fits its
                if sides[i] + matchsticks[idx] <= side_len:
                    sides[i] += matchsticks[idx]
                    
                    if backtracking(idx + 1):
                        return True
                    
                    # this is not the correct place
                    sides[i] -= matchsticks[idx]       
            return False
        
        return backtracking(0)