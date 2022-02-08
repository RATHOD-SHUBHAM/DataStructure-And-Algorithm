# time = O(ca) c is coins a is amount
# sapce = O(a)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        
        # minimum number of coin for having 0 is 0
        dp[0] = 0
        
        # calculate minimum number of coins needed for each amount till target
        for coin in coins:
            for x in range(1, amount+1):
                # eg coin = [1,2,5] and x = 3, i cant use 5 to have amount of 3 
                if coin <= x:
                    dp[x] = min(dp[x] , 1 + dp[ x - coin])
                    
        return dp[amount] if dp[amount] != math.inf else -1