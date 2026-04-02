# Tc: O(n)
# Sc: O(k) , We don't count the output as part of the space complexity, but for each word, we are using some space for the escape character and delimiter.

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        Format: <length>$<word><length>$<word>...
        Example: ["hello", "world"] → "5$hello5$world"
        """
        encoded_str = ""

        for ch in strs:
            len_of_str = len(ch)
            # Prepend each word with its length and a '$' delimiter
            # So we know exactly how many chars to read during decode
            encoded_str += str(len_of_str) + '$' + ch
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string back to a list of strings."""
        n = len(s)
        i = 0  # Main pointer to traverse the encoded string
        decoded_str = []

        while i < n:
            j = i  # Secondary pointer to find the '$' delimiter

            # Move j forward until we hit '$'
            # Everything before '$' is the length of the next word
            while s[j] != '$':
                j += 1
            
            # Extract the length of the upcoming word
            len_of_str = int(s[i : j])

            # Read exactly len_of_str characters after '$'
            char = s[j+1 : j+1+len_of_str]

            decoded_str.append(char)

            # Move i past the current word to start of next encoded chunk
            i = j + 1 + len_of_str
        
        return decoded_str
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))