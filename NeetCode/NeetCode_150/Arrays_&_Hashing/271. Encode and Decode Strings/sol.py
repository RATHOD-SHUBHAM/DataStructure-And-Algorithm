# Tc: O(n)
# Sc: O(k) , We don't count the output as part of the space complexity, but for each word, we are using some space for the escape character and delimiter.

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ""

        for ch in strs:
            len_of_str = len(ch)
            encoded_str += str(len_of_str) + '$' + ch # We don't count the output as part of the space complexity, but for each word, we are using some space for the escape character and delimiter.
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        n = len(s)

        i = 0

        decoded_str = []

        while i < n:

            j = i

            while s[j] != '$':
                j += 1
            
            len_of_str = int(s[i : j])

            char = s[j+1 : j+1+len_of_str]

            decoded_str.append(char)

            i = j + 1 +len_of_str
        
        return decoded_str

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))