class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.split(' ')

        reversed_strs = ""
        n = len(strs)

        for i in reversed(range(n)):
            cur_str = strs[i]

            if cur_str == "":
                continue
            
            if reversed_strs == "":
                reversed_strs += cur_str
            else:
                reversed_strs += ' '+cur_str
        
        return reversed_strs