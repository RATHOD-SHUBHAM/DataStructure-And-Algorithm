from typing import List
# import the List from typing
# it will give a name error if we don't do this
class Solutions():
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
            # consider the first element to be the least value
        min_value = prices[0]
        print("Initial min value is:  ",min_value)
        # profit is always the second element minus the first one
        profit = prices[1] - prices[0]
        print(" Initial profit is: ",profit)

        for i in range(1,len(prices)):
            print(i)
            # we need to check which second element minus the minimum element will give maximum profit
            profit = max(profit,prices[i] - min_value)
            print("profit is : ",profit)
            # we need to keep checking if out current value is the least value
            min_value = min(min_value , prices[i])
            print("The min value is: ",min_value)
        return profit if profit > 0 else 0

def main():
    prices = [7,6,4,3,1]
    s = Solutions()
    my_func = s.maxProfit(prices)
    print(my_func)

if __name__ == '__main__':
    main()