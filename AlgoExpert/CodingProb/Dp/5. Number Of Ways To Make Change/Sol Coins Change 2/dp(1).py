# Logic: Use the current coin and dont use the current coin.
# change the backtacking to recursive method to memoization to dp - thus reducing time complexity
# https://www.youtube.com/watch?v=DJ4a7cmjZY0&ab_channel=BackToBackSWE
# Tc and Sc: O(amount * coins) 

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        curAmount = 0
        curIdx = 0 # represent the coin at current Idx
        
        # total_combination = [0]
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        
        # top down approach
        
        # fill the 0th row with 0
        # because with 0 coin i cannot sum up to any amont
        for col in range(amount + 1):
            dp[0][col] = 0
        # print(dp)
        
        # fill the 0th col with 1
        # because if i dont use any of my coins. i can sum up to amount 0
        for row in range(len(coins) + 1):
            dp[row][0] = 1
        # print(dp)
        
        # starting form 1st row and 1st col
        for coinIdx in range(1, len(coins) + 1):
            for curAmount in range(1, amount + 1):
                # check if I can use my current coin: 
                '''
                If I use my cuurent coint on the curAmount. 
                I should not have a remaining sum < 0
                
                eg if i have 2 coin and my curAmount is 2 - i can use my 2 coins, since 2 - 2 = 0 and it is valied
                
                but if i have 3 coins and my curAmount is 2: then i cant use my coins since 2 - 3  = -1
                ie with a 3 rupee coin, I cant make a 1 ruppee coin
                
                '''
                if curAmount >= coins[coinIdx - 1]: # -1 because in coins we dont have a dummy coin called 0 at 0th idx
                    # we can use the current coin and check the number of ways to make target amount from the remaining amount
                    # we can check without using the current coin
                    remaining_amount = curAmount - coins[coinIdx - 1]
                    # use the current amount + dont use the current amount
                    # if we use the current amount - check on remaining amount
                    dp[coinIdx][curAmount] = dp[coinIdx][remaining_amount] + dp[coinIdx - 1][curAmount]
                
                else:
                    # if i cant use my current amount
                    dp[coinIdx][curAmount] = dp[coinIdx - 1][curAmount]
                    
            # print(dp)
        return dp[-1][-1]