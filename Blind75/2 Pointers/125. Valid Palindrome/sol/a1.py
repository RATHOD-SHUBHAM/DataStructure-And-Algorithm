# Tc: O(n) | Sc: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:

        n = len(s)
        i = 0
        j = n - 1

        while j > i:
            if not s[i].isalnum():
                i += 1

            elif not s[j].isalnum():
                j -= 1

            elif s[i].lower() != s[j].lower():
                return False

            else:
            
                # if s[i] == s[j]
                i += 1
                j -= 1
        
        return True


# Optimal ---------------------------------------------------------

'''
    Rather than traversing each point,
    At once traverse all the non alphanumeric characters.
'''

# Tc: O(n) | Sc: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:

        n = len(s)
        i = 0
        j = n - 1

        while j > i:
            while j > i and not s[i].isalnum():
                i += 1

            while j > i and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            
            # if s[i] == s[j]
            i += 1
            j -= 1
        
        return True