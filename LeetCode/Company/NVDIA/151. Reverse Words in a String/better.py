# Tc and Sc: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.split(" ")
        print(strs)
        
        # get the char from stack
        reversed_strs = ""
        for i in reversed(range(len(strs))):
            cur_char = strs[i]

            if cur_char == "":
                continue
            
            if reversed_strs == "":
                reversed_strs += cur_char
            else:
                reversed_strs += " " + cur_char
        
        print(reversed_strs)
        return reversed_strs