# TC: O(n) and Sc: O(1)
class Solution:
    def makePalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        no_of_operation = 0
        
        while left < right:
            if s[left] != s[right]:
                no_of_operation += 1
                if no_of_operation > 2:
                    return False

            left += 1
            right -= 1

        return True
                