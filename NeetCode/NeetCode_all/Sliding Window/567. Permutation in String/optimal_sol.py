class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
            Match the string in the window
                - If the strings match - there will be 26 character match in the hashmap
        '''
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
        
        # Check the first n1 char
        if s1_count == s2_count:
            return True
        
        # Move the widow and check the string match
        for right in range(n1, n2):
            left = right - n1

            # remove element from left
            left_idx = ord(s2[left]) - ord('a')
            s2_count[left_idx] -= 1

            # add right index
            right_idx = ord(s2[right]) - ord('a')
            s2_count[right_idx] += 1

            if s1_count == s2_count:
                return True
        
        return False