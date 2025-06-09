"""
This wont work:
Your algorithm assumes that stars can always be used as closing parentheses for any remaining open parentheses, but stars can only close parentheses that come before them.

# The real problem: "(**))("

Your code's execution:
s = "(**))("
st = []
star = 0

i=0: '(' -> st = ['(']
i=1: '*' -> star = 1
i=2: '*' -> star = 2
i=3: ')' -> st not empty, so st.pop() -> st = []
i=4: ')' -> st is empty, star > 0, so star -= 1 -> star = 1
i=5: '(' -> st = ['(']

Final: st = ['('], star = 1
len(st) <= star ? 1 <= 1 ? True
Your result: True
Correct result: False

Why this is wrong: The '(' at the end cannot be matched by the '*' characters that came before it, because stars can only act as closing parentheses ')' for opening parentheses that come before them.
In "(**))(", the last '(' appears after all the stars, so none of the stars can close it. But your algorithm assumes any leftover star can close any leftover opening parenthesis, regardless of position.
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        st = []
        star = 0 # keep track of the *

        for para in s:
            if para == "(":
                st.append(para)
            elif para == '*':
                star += 1
            else:
                if st:
                    st.pop()
                elif star > 0:
                    star -= 1
                else:
                    return False
        
        if st:
            return len(st) <= star
        else:
            return True
