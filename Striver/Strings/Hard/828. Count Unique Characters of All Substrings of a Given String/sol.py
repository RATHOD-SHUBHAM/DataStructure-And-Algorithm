# https://www.youtube.com/watch?v=JT1NDR-M_8A&ab_channel=Techdose

# Tc: O(n) | Sc: O(n)

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)

        count = 0

        hashmap = defaultdict(list)

        # Store the positions of each character in the string.
        for i, char in enumerate(s):
            # start of window = -1
            if char not in hashmap:
                hashmap[char].append(-1)

            hashmap[char].append(i)
        
        # print(hashmap)

        for idx, val in hashmap.items():
            val.append(n) # End of window = len(string)

            x = len(val)

            for i in range(1, x-1):
                pre_window = val[i] - val[i-1]
                post_window = val[i+1] - val[i]
                count += pre_window * post_window

        return count