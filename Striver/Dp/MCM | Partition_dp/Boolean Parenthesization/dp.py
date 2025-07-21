#User function Template for python3
class Solution:
    def countWays(self, s):
        # code here
        n = len(s)
        
        # isTrue = True or False
        
        dp = [[[0 for _ in range(2)] for _ in range(n)]for _ in range(n)]
        
        # base case
        for i in range(0, n, 2):  # Only operands
            if s[i] == 'T':
                dp[i][i][1] = 1 # isTrue
            else:
                dp[i][i][0] = 1

        # i = 0 -> n
        # j = n - 1 -> 0
        
        for i in reversed(range(0, n, 2)):
            for j in range(i+2, n, 2): # j must be greater than i
                for isTrue in range(2):
                    ways = 0
                    for k in range(i+1, j, 2):
                        leftTrue = dp[i][k - 1][1]# in how many ways can left child be True
                        leftFalse = dp[i][k - 1][0] # in how many ways can left child be False
                        rightTrue = dp[k+1][j][1] # in how many ways can right child be True
                        rightFalse = dp[k+1][j][0] # in how many ways can right child be False
                        
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
                                
                    dp[i][j][isTrue] = ways
        
        return dp[0][n-1][1]