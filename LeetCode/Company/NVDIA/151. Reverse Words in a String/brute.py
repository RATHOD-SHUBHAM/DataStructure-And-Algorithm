class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.split(" ")
        print(strs)

        stack = []

        # Add char to stack
        for i in strs:
            if not stack and i == "":
                continue

            stack.append(i)
        # print(stack)
        
        # get the char from stack
        reversed_strs = ""
        while stack:
            char = stack.pop()

            if char == "":
                continue
            
            if reversed_strs == "":
                reversed_strs += char
            else:
                reversed_strs += " "+char
        
        print(reversed_strs)
        return reversed_strs