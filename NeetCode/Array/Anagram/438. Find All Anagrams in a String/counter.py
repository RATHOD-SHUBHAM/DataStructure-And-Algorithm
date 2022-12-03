# Tc and Sc: O(n) | O(p)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns = len(s)
        np = len(p)
        
        op = []
        
        # initializing counter
        s_counter = collections.Counter()
        p_counter = collections.Counter(p)
        
        # print(p_counter)
        
        # check every element in s
        for i in range(ns):
            # Add the current element to the counter
            s_counter[s[i]] += 1
            
            # check the window size
            if i >= np:
                idx_before_widow = i - np # get the window element
                
                # if the element was seen only 1s. remove it from count
                if s_counter[s[idx_before_widow]] == 1:
                    del s_counter[s[idx_before_widow]]
                else:
                    # dcrease the count if seen more than once
                    s_counter[s[idx_before_widow]] -= 1
                    
            # compare the 2 counters
            if s_counter == p_counter:
                start_idx = i - np + 1
                op.append(start_idx)
                
        return op
                    