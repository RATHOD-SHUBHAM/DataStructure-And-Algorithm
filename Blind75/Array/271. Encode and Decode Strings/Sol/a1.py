# Encode and Decode with a non ascii character
# Tc: O(n) | Sc: O(k)

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # Encode with a non ascii character
        enc = 'å'.join(strs)
        # print(enc)
        return enc
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        dec = s.split('å')
        # print(dec)
        return dec
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))