# Tc and Sc: O(n)

# concept of monotonic stack
# logic: Everytime i look at the stack. I should get my next smaller element.

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        answer = [-1] * n
        stack = []
        
        for i in reversed(range(n)):
            # pop all the value that is greater than my current element
            while stack and stack[-1] > prices[i]:
                stack.pop()
                
            # if there is any element in my stack - then that is smaller than my current element
            if stack:
                answer[i] = prices[i] - stack[-1]
            else:
                answer[i] = prices[i]
                
            stack.append(prices[i]) # append it to stack, as we may not be sure that this element could possibly be the smaller element for next value.
        
        return answer