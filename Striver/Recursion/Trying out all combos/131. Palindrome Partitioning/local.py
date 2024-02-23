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
        
        # Partition
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