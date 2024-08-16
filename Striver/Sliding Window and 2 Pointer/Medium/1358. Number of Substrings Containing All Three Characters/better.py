class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        count = 0

        for i in range(n):
            char_set = set()

            for j in range(i, n):
                char_set.add(s[j])

                if len(char_set) == 3:
                    '''
                        If there are 3 unique character found, we dont need to traverse further.
                    '''
                    count += 1 + (n - 1 - j)
                    break
        
        return count