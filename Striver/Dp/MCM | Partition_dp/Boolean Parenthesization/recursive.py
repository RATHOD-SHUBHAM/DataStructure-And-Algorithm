#User function Template for python3
class Solution:
    def countWays(self, s):
        # code here
        n = len(s)
        
        i = 0
        j = n - 1
        
        isTrue = 1 # we need to count no of ways expression can be true
        
        return self.recursion(i, j, isTrue, s)
    
    def recursion(self, i, j, isTrue, s):
        # base case
        if i > j:
            return 0
        
        if i == j:
            if isTrue:
                if s[i] == 'T':
                    return 1
                else:
                    return 0
            else:
                if s[i] == 'F':
                    return 1
                else:
                    return 0
        
        ways = 0
        for k in range(i+1, j, 2):
            leftTrue = self.recursion(i, k - 1, True, s) # in how many ways can left child be True
            leftFalse = self.recursion(i, k - 1, False, s) # in how many ways can left child be False
            rightTrue = self.recursion(k + 1, j, True, s) # in how many ways can right child be True
            rightFalse = self.recursion(k + 1, j, False, s) # in how many ways can right child be False
            
            op = s[k]
            
            if op == '&':
                if isTrue:
                    # only way for and to be true is if left and right child are true
                    ways += leftTrue * rightTrue
                else:
                    # False = 0 & 0, 0 & 1,  1 & 0
                    ways += (leftFalse * rightFalse) + (leftFalse * rightTrue) + (leftTrue * rightFalse)
            elif op == '|':
                if isTrue:
                    # True: 1 or 1, 1 or 0 , 0 or 1
                    ways += (leftTrue * rightTrue) + (leftTrue * rightFalse) + (leftFalse * rightTrue)
                else:
                    # False : 0 or 0
                    ways += leftFalse * rightFalse
            elif op == '^':
                if isTrue:
                    # True = 1 ^ 0 , 0 ^ 1
                    ways += (leftTrue * rightFalse) + (leftFalse * rightTrue)
                else:
                    # False = 0 ^ 0, 1 ^ 1
                    ways += (leftTrue * rightTrue) + (leftFalse * rightFalse)
                    
        return ways
        
        