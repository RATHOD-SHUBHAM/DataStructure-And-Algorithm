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