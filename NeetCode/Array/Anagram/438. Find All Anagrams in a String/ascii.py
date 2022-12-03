# TC: O(n)
# sc: O(k): 26 character: O(1)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns = len(s)
        np = len(p)
        
        op = []
        
        s_ascii = [0] * 26
        p_ascii = [0] * 26
        
        # increase the count for that particular char
        for i in range(np):
            ascii_val = ord(p[i]) - ord("a")
            # print(ascii_val)
            p_ascii[ascii_val] += 1
            
        
        # for every character in s
        for i in range(ns):
            ascii_val = ord(s[i]) - ord("a") 
            s_ascii[ascii_val] += 1
            
            # if i moves out of window size
            if i >= np:
                idx_out_of_window = i - np
                ascii_ele = ord(s[idx_out_of_window]) - ord("a")
                
                if s_ascii[ascii_ele] > 0:
                    s_ascii[ascii_ele] -= 1
            
            if s_ascii == p_ascii:
                start_idx = i - np + 1
                op.append(start_idx)

                
        return op
                
        