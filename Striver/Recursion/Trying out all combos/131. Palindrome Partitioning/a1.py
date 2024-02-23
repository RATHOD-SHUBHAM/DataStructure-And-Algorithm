class Solution:
    def __init__(self):
        self.result = []

    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(string, left, right):
            
            while left <= right:
                if string[left] != string[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True

        def backTrack(left, st):

            if left >= len(s):
                self.result.append(st.copy())
                return
            
            # Create Partition
            for right in range(left, len(s)):
                # check if the partition till now is palindrome
                if isPalindrome(s, left, right):
                    st.append(s[left : right + 1])
                    backTrack( right + 1, st)
                    st.pop()
                
            return
        
        st = []
        left = 0
        backTrack(left, st)

        return self.result

# ------------------------------------------------------------------------

class Solution:
    def __init__(self):
        self.result = []

    def partition(self, s: str) -> List[List[str]]:
        st = []
        i = 0
        self.backTrack(i, st, s)

        return self.result
    
    def backTrack(self, left, st, s):
        # basecase
        if left >= len(s):
            self.result.append(st.copy())
            return
        
        # Partition Method
        for right in range(left, len(s)):
            if self.isPalindrome(left, right, s):
                st.append(s[left : right + 1])
                self.backTrack(right + 1, st, s)
                st.pop()
        return

    def isPalindrome(self, left, right, s):
        while left <= right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True