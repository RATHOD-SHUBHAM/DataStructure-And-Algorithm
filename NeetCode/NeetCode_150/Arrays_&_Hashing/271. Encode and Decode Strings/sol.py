class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        n = len(strs)

        new_str = ""

        for s in strs:
            s_len = len(s)
            new_str += str(s_len) + '$' + s
        
        return new_str
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        n = len(s)

        strs = []

        i = 0

        while i < n:
            j = i

            while s[j] != '$':
                j += 1
                

            s_len = int(s[i : j])

            new_str = s[j+1 : j + 1 + s_len]

            strs.append(new_str)

            i = j + 1 + s_len
        
        
        return strs
            


        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))