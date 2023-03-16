# Tc: O(coins * amount) | Sc: O(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for _ in range(amount + 1)]
        dp[0] = 0
        
            
        # dp
        for coinIdx in range(len(coins)):
            for curAmount in range(1, amount + 1):
                if curAmount >= coins[coinIdx]:
                    # if i use the current amount - check for my remaining amount
                    remainingAmount = curAmount - coins[coinIdx]
                    takeCoin = 1 + dp[remainingAmount]
                    dontTakeCoin = 0 + dp[curAmount]
                    dp[curAmount] = min(takeCoin, dontTakeCoin)
                else:
                    dp[curAmount] =  dp[curAmount]
                    
        return dp[-1] if dp[-1] != math.inf else -1