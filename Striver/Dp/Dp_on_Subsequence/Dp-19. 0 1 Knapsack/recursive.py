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

 

