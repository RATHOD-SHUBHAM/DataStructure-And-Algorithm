# Tc and Sc: O(n)

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)

        stack = []

        op = [None] * n

        for i in reversed(range(n)):
            cur_price = prices[i]

            while stack and cur_price < stack[-1]:
                stack.pop()
            
            if not stack:
                op[i] = cur_price # No discount
            else:
                dis_price = cur_price - stack[-1]
                op[i] = dis_price
            
            stack.append(cur_price)
        
        return op