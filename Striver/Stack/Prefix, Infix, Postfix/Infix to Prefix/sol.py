# Tc and Sc: O(n)

class Solution:
    def prededence(self, ch):
        if ch == '^':
            return 3
        elif (ch == '*' or ch == '/'):
            return 2
        elif (ch == '+' or ch == '-'):
            return 1
        else:
            return 0

    
    def InfixtoPostfix(self, exp):
        '''
            Postfix in controlled Environment
        '''
        n = len(exp)

        st = []
        op = []

        i = 0

        while i < n:
            ch = exp[i]

            if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9'):
                '''
                    ch.isalpha() or ch.isdigit()
                '''
                # This is a Operand
                op.append(ch)
            
            elif ch == '(':
                st.append(ch)
            
            elif ch == ')':
                while st and st[-1] != '(':
                    val = st.pop()
                    op.append(val)
                # pop out the opening bracket too
                st.pop()
            
            else:
                '''
                i. if ^ : pop, if ^ has less than or equal to predecence top of stack.
                ii. Operator: pop, if current operator has less precedence than top of stack.
                '''
                if ch == '^':
                    while st and (self.prededence(ch) <= self.prededence(st[-1])):
                        val = st.pop()
                        op.append(val)
                else:
                    while st and (self.prededence(ch) < self.prededence(st[-1])):
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
    

    def InfixtoPrefix(self, exp):
        # Step 1: Reverse the expression
        exp = exp[::-1]

        # Step 2: Swap the brackets
        for i in range(len(exp)):
            if exp[i] == '(':
                exp[i] = ')'

            elif exp[i] == ')':
                exp[i] = '('

            else:
                continue
        
        
        # Step 3: Infix to Postfix
        exp = self.InfixtoPostfix(exp)

        # Step 4: Reverse the Expression
        exp = exp[::-1]

        return exp


if __name__ == '__main__':
    obj = Solution()
    
    exp = "x+y*z/w+u"
     
    # Function call
    print(obj.InfixtoPrefix(exp))