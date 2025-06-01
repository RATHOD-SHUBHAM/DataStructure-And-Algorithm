from os import *
from sys import *
from collections import *
import math

## Read input as specified in the question.
## Print output as specified in the question.

class Solution(object):
    def knapsack(self, W : int, weights : list[int], values : list[int], N : int): 
        n = len(weights)

        idx = n - 1

        return self.recursion(idx, weights, values, W)
    
    def recursion(self, idx, weights, values, W):
        # base case
        if idx == 0:
            if weights[0] <= W:
                return values[0]
            else:
                return 0
        
        # Logic
        if weights[idx] <= W:
            take = values[idx] + self.recursion(idx - 1, weights, values, W - weights[idx])
        else:
            take = -math.inf

        no_take = 0 + self.recursion(idx - 1, weights, values, W )

        return max(take, no_take)




# Input 
def takeInput():

    T = int(input())

    for _ in range(T):

        N = int(input())

        weights = list(map(int, input().split()))

        values = list(map(int, input().split()))

        W = int(input())

        # print(N, weights, values, W)

 

        if len(weights)!=N or len(values)!=N:

            print("Error: The number of weights and values should be equal to N.")

            continue

 

        max_value = Solution().knapsack(W, weights, values, N)

        print(max_value)

 

if __name__ == "__main__":

    takeInput()

 

# --------------------------- Memoization ---------------------------

from os import *
from sys import *
from collections import *
import math

## Read input as specified in the question.
## Print output as specified in the question.

class Solution(object):
    def knapsack(self, W : int, weights : list[int], values : list[int], N : int): 
        n = len(weights)

        idx = n - 1

        memo = {}

        return self.recursion(idx, memo, weights, values, W)
    
    def recursion(self, idx, memo, weights, values, W):
        # base case
        if idx == 0:
            if weights[0] <= W:
                return values[0]
            else:
                return 0
        
        if (idx, W) in memo:
            return memo[(idx, W)]
        
        # Logic
        if weights[idx] <= W:
            take = values[idx] + self.recursion(idx - 1, memo, weights, values, W - weights[idx])
        else:
            take = -math.inf

        no_take = 0 + self.recursion(idx - 1, memo, weights, values, W )

        memo[(idx, W)] = max(take, no_take)

        return memo[(idx, W)]
    
# ------------------------ Tabulation ------------------------

from os import *
from sys import *
from collections import *
import math

## Read input as specified in the question.
## Print output as specified in the question.

class Solution(object):
    def knapsack(self, W : int, weights : list[int], values : list[int], N : int): 
        n = len(weights)

        dp = [[0 for _ in range(W+1)]for _ in range(n)]

        # Base case
        for cur_weight in range(W+1):
            if weights[0] <= cur_weight:
                dp[0][cur_weight] = values[0]
        
        # Logic
        for idx in range(1, n):
            for cur_weight in range(W+1):
                
                if weights[idx] <= cur_weight:
                    take = values[idx] + dp[idx - 1][cur_weight - weights[idx]]
                else:
                    take = -math.inf

                no_take = 0 + dp[idx - 1][cur_weight]

                dp[idx][cur_weight] = max(take, no_take)

        return dp[n-1][W]
    
# -------------------------- Space Optimization ------------------------

from os import *
from sys import *
from collections import *
import math

## Read input as specified in the question.
## Print output as specified in the question.

class Solution(object):
    def knapsack(self, W : int, weights : list[int], values : list[int], N : int): 
        n = len(weights)

        dp = [0 for _ in range(W+1)]

        # Base case
        for cur_weight in range(W+1):
            if weights[0] <= cur_weight:
                dp[cur_weight] = values[0]
        
        # Logic
        for idx in range(1, n):
            temp = [0 for _ in range(W+1)]

            for cur_weight in range(W+1):
                if weights[idx] <= cur_weight:
                    take = values[idx] + dp[cur_weight - weights[idx]]
                else:
                    take = -math.inf

                no_take = 0 + dp[cur_weight]

                temp[cur_weight] = max(take, no_take)
            
            dp = temp

        return dp[W]