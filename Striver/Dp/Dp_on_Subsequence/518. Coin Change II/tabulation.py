class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[0 for _ in range(amount + 1)] for _ in range(n)]

        # dp[i][0] = 1 means: "There is exactly 1 way to make amount 0 using coins 0 through i"
        # That one way is: use zero coins (the empty set).

        # for i in range(n):
        #     dp[i][0] = 1

        # for target in range(1, amount + 1):
        #     if target % coins[0] == 0:
        #         dp[0][target] =  1

        # OR
        
        for target in range(amount + 1):
            if target % coins[0] == 0:
                dp[0][target] =  1
        
        for idx in range(1, n):
            for target in range(amount + 1):
                if target >= coins[idx]:
                    # Take the coins, then try again by taking the same coin
                    take = dp[idx][target - coins[idx]]
                else:
                    take = 0
                
                # Dont take this coin, move to next index
                no_take = dp[idx - 1][target]

                dp[idx][target] = take + no_take
        
        return dp[n-1][amount]