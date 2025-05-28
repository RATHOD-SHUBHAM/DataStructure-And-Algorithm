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

 

