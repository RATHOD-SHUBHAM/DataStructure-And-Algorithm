"""

20. Valid Parentheses
Easy


Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for paranthesis in s:

            if paranthesis in dict:
                # if there is a opening bracket then there must be a closing bracket before it.
                top_value = stack.pop() if stack else '#'

                if top_value != dict[paranthesis]: return False

            else:
                stack.append(paranthesis)
        # not stack will return boolean value true when the list is empty
        # print(not stack)

        return not stack