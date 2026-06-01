# Tc: O(n) | Sc: O(n) - due to recursive stack space
# Subarray creates a whole new string


class Solution:

    def palindrome(self, s, flag):
        n = len(s)

        i = 0
        j = n - 1

        while i < j:
            if s[i] != s[j]:
                if flag == False: # here we have a chance of deleting a character and checking if the string can be a palindrome
                    flag = True # Tell the subarray that we have already deleted a character, so dont even thing about it

                    child_1 = self.palindrome(s[i : j], flag) # subarray excluding j
                    child_2 = self.palindrome(s[i + 1 : j + 1], flag) # subarray excluding i

                    # Check even if one of the subarray can form palindrome
                    if child_1 == True or child_2 == True:
                        return True
                    else:
                        return False
                    
                else:
                    # There is no option to delete a character - and the elements anyways dont match
                    return False

            else:
                # Elements are the same - move and compare others
                i += 1
                j -= 1
        
        return True


    def validPalindrome(self, s: str) -> bool:
        flag = False # keeps track to see if we have previously deleted a char or not
        return self.palindrome(s, flag)
    

# ======================================================================================================
# Improved Space Complexity
# ======================================================================================================

# Slicing creates new strings of size ~n
# Tc: O(n) | Sc:O(1)

class Solution:

    def palindrome(self, s, i, j, flag):
        
        while i < j:
            if s[i] != s[j]:
                if flag == False: # here we have a chance of deleting a character and checking if the string can be a palindrome
                    flag = True # Tell the subarray that we have already deleted a character, so dont even thing about it

                    child_1 = self.palindrome(s,i, j-1, flag) # subarray excluding j
                    child_2 = self.palindrome(s, i+1, j, flag) # subarray excluding i

                    # Check even if one of the subarray can form palindrome
                    if child_1 == True or child_2 == True:
                        return True
                    else:
                        return False
                    
                else:
                    # There is no option to delete a character - and the elements anyways dont match
                    return False

            else:
                # Elements are the same - move and compare others
                i += 1
                j -= 1
        
        return True


    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        i = 0
        j = n - 1

        flag = False # keeps track to see if we have previously deleted a char or not
        return self.palindrome(s, i, j, flag)