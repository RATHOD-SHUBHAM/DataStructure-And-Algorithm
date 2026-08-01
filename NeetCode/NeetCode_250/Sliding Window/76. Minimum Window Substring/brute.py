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
                
                # reduce the count: mark it as seen
                dic[s[j]] -= 1
        
        return min_str

                
