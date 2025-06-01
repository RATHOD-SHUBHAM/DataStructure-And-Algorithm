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