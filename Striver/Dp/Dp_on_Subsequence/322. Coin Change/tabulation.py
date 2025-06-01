class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [[math.inf for _ in range(amount + 1)]for _ in range(n)]

        # base case
        # # If i dont pick any coins, we can form amount of zero
        for i in range(n):
            dp[i][0] = 0
        
        for target in range(1, amount + 1):
            if target % coins[0] == 0:
                dp[0][target] = target // coins[0]
        

        for idx in range(1, n):
            for target in range(amount + 1):
                if target >= coins[idx]:
                    # Take the coins, then try again by taking the same coin
                    take = 1 + dp[idx][target - coins[idx]]
                else:
                    take = math.inf
                
                # Dont take this coin, move to next index
                no_take = 0 + dp[idx - 1][target]

                dp[idx][target] = min(take, no_take)
        
        no_of_coins = dp[n-1][amount]

        if no_of_coins == math.inf:
            return -1
        else:
            return no_of_coins