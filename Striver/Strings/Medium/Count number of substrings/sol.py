class Solution:
    def helper(self, s, k):
        n = len(s)
        
        left = right = cnt = no_of_substring = 0
        
        freq = [0] * 26
        
        while right < n:
            freq[ord(s[right]) - ord('a')] += 1
            
            if freq[ord(s[right]) - ord('a')] == 1:
                # if this is the first occurance
                cnt += 1
            
            
            while cnt > k:
                # move the substring window
                freq[ord(s[left]) - ord('a')] -= 1
                # Check if the character can be removed from substring
                if freq[ord(s[left]) - ord('a')] == 0:
                    cnt -= 1
                
                left += 1
            
            
            # Get the number of current substring and add to previous one
            no_of_substring += right - left + 1
            
            right += 1
        
        return no_of_substring       
        
        
    def substrCount (self,s, k):
        # Atmost k substring
        atmost_k = self.helper(s, k)
        atmost_k_minus_one = self.helper(s, k-1)
        
        return atmost_k - atmost_k_minus_one