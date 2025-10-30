# Tc: O(n) | Sc: O(n)

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for s in strs:
            len_of_s = len(s)
            # Encoding: len_of_word  + # + word: 5#hello
            new_word = str(len_of_s) + '#' + s
            res.append(new_word)

        print(res)
        print("".join(res))
        return "".join(res)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        ans = []
        '''
            Get the Length of the character
            Move to the pound
            Slice everything after pound till the length of character
        '''

        while i < len(s):
            j = i

            # go the hash value
            while s[j] != '#':
                j += 1
            
            len_of_s = int(s[i : j])
            word = s[j+1 : j+1 + len_of_s]

            ans.append(word)
            # print(ans)

            i = j + 1 + len_of_s
        
        return ans
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))