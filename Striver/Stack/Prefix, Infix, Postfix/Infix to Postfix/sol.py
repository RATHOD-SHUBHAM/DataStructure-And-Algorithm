# Tc and Sc: O(n)

class Solution:
    def precedence(self, ch):
        if ch == '^':
            return 3
        elif (ch == '*' or ch == '/'):
            return 2
        elif (ch == '+' or ch == '-'):
            return 1
        else:
            return 0
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        #code here
        n = len(exp)
        
        i = 0
        
        st = []
        
        op = []
        
        while i < n:
            ch = exp[i]
            
            if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9'):
                '''
                    ch.isalpha() or ch.isdigit()
                '''
                # This is a Operand
                op.append(ch)
            elif ch == '(':
                # Append Opening Bracket to stack amd move on
                st.append(ch)
            elif ch == ')':
                while st and st[-1] != '(':
                    val = st.pop()
                    op.append(val)
                # pop out the opening bracket too
                st.pop()
            else:
                '''
                    Push to the stack if current character has higher precedence than the top of stack operator
                '''
                while st and (self.precedence(ch) <= self.precedence(st[-1])):
                    # If current character has lesser precedence than the top of stack
                    val = st.pop()
                    op.append(val)
                
                # Push the current operator to stack
                st.append(ch)
            
            i += 1
            
        while st:
            # pop the remaining element from stack
            val = st.pop()
            op.append(val)
        
        return "".join(op)
    

if __name__ == '__main__':
    obj = Solution()
    
    exp = "a+b*(c^d-e)^(f+g*h)-i"

    # Function call
    print(obj.InfixtoPostfix(exp))