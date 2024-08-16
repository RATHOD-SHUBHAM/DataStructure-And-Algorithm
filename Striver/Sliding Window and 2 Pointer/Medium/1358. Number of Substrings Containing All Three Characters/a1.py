# ---------------  Brute Force ---------------

# Tc:O(n^2) | Sc:O(1)

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        count = 0

        for i in range(n):
            char_set = set()

            for j in range(i, n):
                char_set.add(s[j])

                if len(char_set) >= 3:
                    count += 1
        
        return count
    
# ---------------  Better ---------------

# Tc:O(n^2) | Sc:O(1)

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
    

# ---------------  Optimal ---------------

'''
# Backward traversal of pointers
    From a given point(right), check to the left if it forms a window  that has the 3 unique characters
'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        last_seen = {
                        'a': -1,
                        'b' : -1,
                        'c' : -1
                    }

        no_of_substring = 0
        
        for i in range(n):
            cur_char = s[i]

            # Update to recently seen
            last_seen[cur_char] = i

            if -1 in last_seen.values():
                continue
            
            # Else: Three unique character found
            '''
                get the window of unique character
            '''
            right = i
            left = min(last_seen.values())

            left_most_window_character_idx = left

            no_of_substring += left_most_window_character_idx + 1
        
        return no_of_substring