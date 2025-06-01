class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        idx = n - 1

        no_of_coins = self.recursion(idx, coins, amount)

        if no_of_coins == math.inf:
            return -1
        else:
            return no_of_coins
    
    def recursion(self, idx, arr, target):
        if idx == 0:
            # Take the first coin as many times as possible
            if target % arr[0] == 0:
                return target // arr[0]
            else:
                return math.inf
        
        if target >= arr[idx]:
            # Take the coins, then try again by taking the same coin
            take = 1 + self.recursion(idx, arr, target - arr[idx])
        else:
            take = math.inf
        
        # Dont take this coin, move to next index
        no_take = 0 + self.recursion(idx - 1, arr, target)

        return min(take, no_take)

# ---------------------- Memoization ----------------------
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        idx = n - 1

        memo = {}

        no_of_coins = self.recursion(idx, memo, coins, amount)

        if no_of_coins == math.inf:
            return -1
        else:
            return no_of_coins
    
    def recursion(self, idx, memo, arr, target):
        if idx == 0:
            if target % arr[0] == 0:
                return target // arr[0]
            else:
                return math.inf
        
        if (idx, target) in memo:
            return memo[(idx, target)]
        
        if target >= arr[idx]:
            # Take the coins, then try again by taking the same coin
            take = 1 + self.recursion(idx, memo, arr, target - arr[idx])
        else:
            take = math.inf
        
        # Dont take this coin, move to next index
        no_take = 0 + self.recursion(idx - 1, memo, arr, target)

        memo[(idx, target)] = min(take, no_take)

        return memo[(idx, target)]
    
# ---------------------- Tabulation ----------------------
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
        
# ---------------------- Space Optimization ----------------------
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [math.inf for _ in range(amount + 1)]

        # base case
        # If i dont pick any coins, we can form amount of zero
        dp[0] = 0
        
        for cur_amount in range(amount+1):
            if cur_amount % coins[0] == 0:
                dp[cur_amount] = cur_amount // coins[0]
        
        for idx in range(1, n):
            temp = [math.inf for _ in range(amount + 1)]
            temp[0] = 0

            for cur_amount in range(1, amount+1):
                # Logic
                if coins[idx] <= cur_amount:
                    take = 1 + temp[cur_amount - coins[idx]]
                else:
                    take = math.inf
                
                no_take = 0 + dp[cur_amount]

                temp[cur_amount] = min(take, no_take)
            
            dp = temp
        
        no_of_coins = dp[amount]

        if no_of_coins == math.inf:
            return -1
        else:
            return no_of_coins