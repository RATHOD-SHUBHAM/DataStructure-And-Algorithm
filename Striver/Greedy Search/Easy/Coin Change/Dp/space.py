class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [math.inf for _ in range(amount + 1)]

        # base case
        # We can never have a coin with zero amount
        dp[0] = 0
        
        for target in range(1, amount + 1):
            if target % coins[0] == 0:
                dp[target] = target // coins[0]
        

        for idx in range(1, n):
            temp = [math.inf for _ in range(amount + 1)]
            
            for target in range(amount + 1):
                if target >= coins[idx]:
                    # Take the coins, then try again by taking the same coin
                    take = 1 + temp[target - coins[idx]]
                else:
                    take = math.inf
                
                # Dont take this coin, move to next index
                no_take = 0 + dp[target]

                temp[target] = min(take, no_take)
            
            dp = temp
        
        no_of_coins = dp[amount]

        if no_of_coins == math.inf:
            return -1
        else:
            return no_of_coins