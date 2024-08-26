# Tc and Sc: O(n)

class Solution:
    def PrefixtoInfix(self, exp):
        n = len(exp)
        
        st = []
        
        i = n - 1 # Iterate in reverse order
        
        while i >= 0:
            ch = exp[i]
            
            if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9'):
                '''
                    ch.isalpha() or ch.isdigit()
                '''
                # This is a Operand
                st.append(ch)
            
            else:
                '''
                    Pop the top 2 operands
                    add operator between the 2 operands
                    Push back to stack
                '''
                ele_1 = st.pop()
                ele_2 = st.pop()
                
                new_str = '(' + ele_1 + ch + ele_2 + ')'
                
                st.append(new_str)
            
            i -= 1
        
        infix_exp = st.pop()
        return infix_exp
    
if __name__ == '__main__':
    obj = Solution()
    
    exp = "*-A/BC-/AKL"
     
    # Function call
    print(obj.PrefixtoInfix(exp))