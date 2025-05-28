class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [0 for _ in range(amount + 1)]

        # dp[0] = 1

        # for target in range(1, amount + 1):
        #     if target % coins[0] == 0:
        #         dp[target] =  1


        for target in range(amount + 1):
            if target % coins[0] == 0:
                dp[target] =  1

        
        for idx in range(1, n):
            temp = [0 for _ in range(amount + 1)]
            temp[0] = 1

            for target in range(amount + 1):
                if target >= coins[idx]:
                    # Take the coins, then try again by taking the same coin
                    take = temp[target - coins[idx]]
                else:
                    take = 0
                
                # Dont take this coin, move to next index
                no_take = dp[target]

                temp[target] = take + no_take
            
            dp = temp

        
        return dp[amount]