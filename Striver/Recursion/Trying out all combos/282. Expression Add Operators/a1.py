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
    

# ------------------------------------------------------------------------------------------------------------------------
    
# Handling Multiplication
    

class Solution:
    def __init__(self):
        self.result = []

    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)

        # Helper function ------------------------------
        def backTrack(start, cur_str, cur_sum, prev_num):
            # basecase
            if start == n and cur_sum == target:
                print(cur_str)
                val = "".join(cur_str.copy())
                self.result.append(val)
                return
            
            # if the target is not matched
            if start >= n:
                return
            

            # logic
            for i in range(start , n):
                # Check if there is a leading zero
                if i > start and num[start] == '0':
                    return

                cur_sub_str = num[start : i + 1]
                cur_num = int(cur_sub_str)

                if not cur_str:
                    # if this is the first element
                    backTrack(i + 1, [cur_sub_str], cur_num, cur_num)
                else:
                    # add
                    backTrack(i + 1, cur_str + ['+'] + [cur_sub_str], cur_sum + cur_num, cur_num)

                    # sub
                    backTrack(i + 1, cur_str + ['-'] + [cur_sub_str], cur_sum - cur_num, -cur_num)

                    # mul
                    backTrack(i + 1, cur_str + ['*'] + [cur_sub_str], cur_sum - prev_num + cur_num * prev_num, prev_num * cur_num)
            
            return


        # Main function ------------------------------
        cur_sum = 0
        cur_str = []
        prev_num = 0
        idx = 0
        backTrack(idx, cur_str, cur_sum, prev_num)

        return self.result