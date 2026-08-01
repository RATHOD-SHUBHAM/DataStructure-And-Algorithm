class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        min_str = ""
        min_window_len = math.inf
        

        for i in range(m):
            # reset the variables for every new substring
            dic = collections.defaultdict(int) 
            count = 0

            # This will help to understand and keep track of the char available in t
            for j in range(n):
                dic[t[j]] += 1
            
            for j in range(i, m):
                # Check if there is a occurance of char from t in s
                if dic[s[j]] > 0:
                    count += 1 # if there is a occurance then increase count by one
                
                if count == n:
                    cur_window = (j - i) + 1

                    if cur_window < min_window_len:
                        min_window_len = cur_window
                        min_str = s[i: j+1]
                        break
                
                # reduce the count
                dic[s[j]] -= 1
        
        return min_str

# ==========================            ===========================         ================================

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if n > m:
            return ""

        min_str = ""
        min_window_len = math.inf

        dic = collections.defaultdict(int)

        for i in range(n):
            dic[t[i]] += 1

        left = right = 0
        count = 0

        while right < m:
            # First check if the element exist in t
            if dic[s[right]] > 0:
                count += 1 # if there is a occurance then increase count by one

            dic[s[right]] -= 1 # mark it as seen

            while count == n:
                cur_window = (right - left) + 1

                if cur_window < min_window_len:
                    min_window_len = cur_window
                    min_str = s[left : right + 1]
                
                # Shrink the window
                dic[s[left]] += 1 # mark this as unseen
                if dic[s[left]] > 0:
                    count -= 1
                
                left += 1

            
            right += 1 # Expand the window
    
        return min_str

        

        