'''
But, this approach is bound to fail because the * operator takes precedence over + and -. 
The * operator would require the actual previous operand in our expression rather than the current value of the expression. 

Eg: 1 + 2 * 3 = 7 and not 9

How to handle this?
We simply need to keep track of the last operand in our expression and how it modified the expression's value overall so that when we consider the * operator, 
we can reverse the effects of the previous operand and consider it for multiplication. 

'''
class Solution:
    
    def __init__(self):
        self.operators = ['add','sub','mul']
        self.result = []

    def addOperators(self, num: str, target: int) -> List[str]:
        operator = []
        cur_string = []
        n = len(num)

        # Helper function -----------------------------------
        def backtrack(idx, cur_sum):
            # base case
            if idx == n and cur_sum == target:
                final_str = []
                final_str.append(num[0])
                for i in range(len(cur_string)):
                    final_str.append(operator[i])
                    final_str.append(cur_string[i])
                    
                
                val = "".join(final_str)
                self.result.append(val)
                return

            if idx >= n:
                return

            cur_int = int(num[idx])

            for op in self.operators:
                if op == 'add':
                    cur_sum += cur_int
                    operator.append('+')
                    cur_string.append(num[idx])
                elif op == 'sub':
                    cur_sum -= cur_int
                    operator.append('-')
                    cur_string.append(num[idx])
                elif op == 'mul':
                    cur_sum *= cur_int
                    operator.append('*')
                    cur_string.append(num[idx])


                backtrack(idx + 1, cur_sum)
                operator.pop()
                cur_string.pop()
            
            return

        # Main function -----------------------------------
        idx = 1
        cur_sum = int(num[0])
        backtrack(idx, cur_sum)
        return self.result