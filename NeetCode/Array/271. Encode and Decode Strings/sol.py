# ["Hello","World"] : E:"HelloWorld" => D:['Hello','World']
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ""
        
        # build a packet of encoded string 
        # encoded string will contain : len of string , special char ":", and string itself
        # encoded string = [len(string) , ":", string]
        for st in strs:
            len_str = len(st)
            encoded_str += str(len_str) + ":" + st
        
        # print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # Extract the string based in its length
        # get the first occurance of special character
        strs = []
        i = 0
        
        while i < len(s):
            j = i
            
            # look for the first occurance of special character
            while s[j] != ":":
                j += 1
            
            # extract the len
            len_of_str = int(s[i:j])
            
            # extract the number of characters after special characters
            strs.append(s[j + 1 : j + 1 + len_of_str])
            
            i = j + 1 + len_of_str
            
        return strs


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))