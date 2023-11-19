'''

If my previous operator is a + or -,
then i calulate the sum as result.

if my previous operator is a * or /
then i calculate the product or quotient of curNumber and prevNumber

'''


# Time = O(n)
# Space = O(1)

# Dont forget the Bodmas rule

'''
res    output  cur
 3   +   2   *  1


3 + 2 --> res = 3 and output = 2 so that it waits for next element to see if it has to add or do something else

" 3+5 / 2 "
there is space in the front and back. Take care
'''

class Solution:
    def calculate(self, s: str) -> int:
        curNum = output = result = 0
        
        prevOp = "+" # previous Operator
        
        # go through all the element -- should enter loop even for last digit
        for i in range(len(s) + 1):
            # once I cross the last element ill add all the values
            if i < len(s):
                c = s[i]
            else:
                c = "+"
                
            if c == " ": # c = "" is different from c = " "
                continue
                
            if c.isdigit():
                curNum = 10*curNum + int(c) # if num = "12"-> 10*0+1 = 1 -- 10*1+2 = 12
                continue # if there is a digit -- dont do anything
                
            # if c is a operator
            if prevOp == "+":
                result += output
                output = curNum
            elif prevOp == "-":
                result += output
                output = -curNum
            elif prevOp == "*":
                output *= curNum
            elif prevOp == "/":
                output = int(output / curNum )
                
            curNum = 0
            prevOp = c # change the operator as we move front
            
        # once we are done with the loop: add all the value
        return result + output