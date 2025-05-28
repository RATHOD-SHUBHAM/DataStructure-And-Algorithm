class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        idx = n - 1

        no_of_coins = self.recursion(idx, coins, amount)

        return no_of_coins
    
    def recursion(self, idx, arr, target):
        if idx == 0:
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