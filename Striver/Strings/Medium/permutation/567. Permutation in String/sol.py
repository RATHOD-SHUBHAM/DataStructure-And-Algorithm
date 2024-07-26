class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(n1):
            idx1 = ord(s1[i]) - ord('a')
            idx2 = ord(s2[i]) - ord('a')

            s1_count[idx1] += 1
            s2_count[idx2] += 1
        
        if s1_count == s2_count:
            return True
        
        for i in range(n1,  n2):
            left_idx = ord(s2[i - n1]) - ord('a')
            s2_count[left_idx] -= 1

            right_idx = ord(s2[i]) - ord('a')
            s2_count[right_idx] += 1

            if s1_count == s2_count:
                return True

        return False