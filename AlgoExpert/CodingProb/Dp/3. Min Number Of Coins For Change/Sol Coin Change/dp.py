# Tc: O(coins * amount) | Sc: O(coins * amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        
        # when i have 0 coin, i cannout make any amount
        # so the 0th row will be inf
        for col in range(amount + 1):
            dp[0][col] = math.inf
            
        # when i have some coins - I can make 0 amount by not using the coin
        for row in range(len(coins) + 1):
            dp[row][0] = 0
            
        # dp
        for coinIdx in range(1, len(coins) + 1):
            for curAmount in range(1, amount + 1):
                if curAmount >= coins[coinIdx - 1]:
                    # if i use the current amount - check for my remaining amount
                    remainingAmount = curAmount - coins[coinIdx - 1]
                    takeCoin = 1 + dp[coinIdx][remainingAmount]
                    dontTakeCoin = 0 + dp[coinIdx - 1][curAmount]
                    dp[coinIdx][curAmount] = min(takeCoin, dontTakeCoin)
                else:
                    dp[coinIdx][curAmount] =  dp[coinIdx - 1][curAmount]
                    
        return dp[-1][-1] if dp[-1][-1] != math.inf else -1