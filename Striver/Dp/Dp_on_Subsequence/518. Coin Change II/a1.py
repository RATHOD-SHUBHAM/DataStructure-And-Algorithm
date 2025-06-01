class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        idx = n - 1

        no_of_coins = self.recursion(idx, coins, amount)

        return no_of_coins
    
    def recursion(self, idx, arr, target):
        if idx == 0:
            # We can take the first coin any number of times
            if target % arr[0] == 0:
                return 1
            else:
                return 0
        
        if target >= arr[idx]:
            # Take the coins, then try again by taking the same coin
            take = self.recursion(idx, arr, target - arr[idx])
        else:
            take = 0
        
        # Dont take this coin, move to next index
        no_take = self.recursion(idx - 1, arr, target)

        return take + no_take
    
# ---------------------- Memoization ----------------------
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        idx = n - 1

        memo = {}

        no_of_coins = self.recursion(idx, memo, coins, amount)

        return no_of_coins
    
    def recursion(self, idx, memo, arr, target):
        if idx == 0:
            if target % arr[0] == 0:
                return 1
            else:
                return 0
        
        if (idx, target) in memo:
            return memo[(idx, target)]
        
        if target >= arr[idx]:
            # Take the coins, then try again by taking the same coin
            take = self.recursion(idx, memo, arr, target - arr[idx])
        else:
            take = 0
        
        # Dont take this coin, move to next index
        no_take = self.recursion(idx - 1, memo, arr, target)

        memo[(idx, target)] =  take + no_take

        return memo[(idx, target)]

# ---------------------- Tabulation ----------------------
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[0 for _ in range(amount + 1)] for _ in range(n)]

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
    
# ---------------------- Space Optimization ----------------------

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