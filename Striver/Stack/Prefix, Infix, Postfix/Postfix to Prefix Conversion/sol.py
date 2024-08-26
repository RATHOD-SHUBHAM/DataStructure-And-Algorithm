# Tc and Sc: O(n)

class Solution:
    def PostfixtoPrefix(self, exp):
        n = len(exp)
        
        st = []
        
        i = 0
        
        while i < n:
            ch = exp[i]
            
            if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9'):
                '''
                    ch.isalpha() or ch.isdigit()
                '''
                # This is a Operand
                st.append(ch)
            
            else:
                '''
                Pop the top 2 Operands
                Add operator in the front
                Push back to stack
                '''
                ele_2 = st.pop()
                ele_1 = st.pop()
                
                new_string = ch + ele_1 + ele_2
                
                st.append(new_string)
            
            i += 1
        
        prefix_exp = st.pop()
        return prefix_exp
    

if __name__ == '__main__':
    obj = Solution()
    
    exp = "ABC/-AK/L-*"
     
    # Function call
    print(obj.PostfixtoPrefix(exp))