# Tc: O(log(n)) and Sc: O(1)
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s) < 3:
            return 0

        elif len(s) == 3:
            return 1 if s[0]==s[2] else 0
                
        else:
            num_of_palindromes = 0
            # get all the characters
            unique = list(set(s))
            
            
            for char in unique:
                count = s.count(char)
                # check if there is a second element
                if count > 1:
                    # find first and last index of char in s
                    a_index = s.index(char)
                    c_index = s.rindex(char)
                    
                    # find num of unique chars between the two indeces 
                    between = s[a_index+1:c_index]
                    unique_char_in_btn = list(set(between))
                    # no of unique character in between
                    num_of_palindromes += len(unique_char_in_btn)
                
            return num_of_palindromes