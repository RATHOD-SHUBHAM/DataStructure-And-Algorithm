class Solution:
    def __init__(self):
        self.subseq = []

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        idx = n - 1

        st = []

        self.recursion(idx, st, s)

        # print(self.subseq)

        return self.longest_palindrome()

    
    def recursion(self, idx, st, s):
        # base case
        if idx < 0:
            # strng = st[::]
            # f_strng = "".join(strng)
            # self.subseq.append(f_strng)
            self.subseq.append("".join(st[::]))
            return
        
        # Take
        st.append(s[idx])
        self.recursion(idx-1, st, s)

        # No_Take
        st.pop()
        self.recursion(idx-1, st, s)

        return
    
    
    def longest_palindrome(self):
        max_len = 0

        for st in self.subseq:
            if self.valid_palindrome(st):
                cur_len = len(st)
                max_len = max(max_len, cur_len)
        
        return max_len

    def valid_palindrome(self, st):
        n = len(st)

        left = 0
        right = n-1

        while left <= right:
            if st[left] != st[right]:
                return False
            
            left += 1
            right -= 1
        
        return True