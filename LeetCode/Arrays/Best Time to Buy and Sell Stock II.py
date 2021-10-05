from typing import List

# basically i subtract the previous value with current value and save the result in profit
class Solutions():
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 2:
            return 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i - 1]
        return profit if profit > 0 else 0


def main():
    prices = [1, 2, 3, 4, 5]
    s = Solutions()
    my_func = s.maxProfit(prices)
    print(my_func)


if __name__ == '__main__':
    main()
