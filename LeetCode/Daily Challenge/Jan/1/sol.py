# Tc and Sc: O(N)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_pattern = list(pattern)
        list_s = s.split(" ")
        dic = {}
        
        # if the pattern and word len are differnet then we cant compare
        if len(list_s) != len(list_pattern):
            return False
        
        for i in range(len(list_pattern)):
            # if the pattern and word have same character then dictionary will get confused
            cur_pattern = "pattern_" + list_pattern[i]
            cur_char = "word_" + list_s[i]
            
            if cur_pattern not in dic:
                dic[cur_pattern] = i
            
            if cur_char not in dic:
                dic[cur_char] = i
                
            # if the pattern and word have different index then there is a miss match
            if dic[cur_pattern] != dic[cur_char]:
                return False
            
        return True
            
            