'''
s1 = "adc",  

window_size = 3

freq = {
    a : 1
    d : 1
    c : 1
}

i + window_size = 5 + 3 = 8
s2 = "d c d a"
      0 1 2 3 
      i
        j

copy_freq = {
    a : 1
    d : 0
    c : 0
}
        

'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = window_size = len(s1)
        n2 = len(s2)

        # Grab all the value of s1
        freq = {}
        for i in range(n1):
            cur_val = s1[i]

            if cur_val not in freq:
                freq[cur_val] = 0
            
            freq[cur_val] += 1
        
        # print(freq)

        # Iterate and check the second array for permutation
        copy_freq = freq.copy()
        # print(copy_freq)

        i = 0

        while i < (n2 - n1 + 1):
            
            cur_val = s2[i]

            if cur_val not in copy_freq:
                i += 1
                continue

            # if cur_val in copy_freq:
            j = i

            while j < i + window_size:
                
                # If the value is not part of s1
                if s2[j] not in copy_freq:
                    i = j + 1
                    # Reset the freq table
                    copy_freq = freq.copy()
                    break
                
                # This value is seen again so move a step to ignore the dulicate
                if copy_freq[s2[j]] == 0:
                    i = i + 1
                    # Reset the freq table
                    copy_freq = freq.copy()
                    break
                
                copy_freq[s2[j]] -= 1

                j += 1
            
            # If J has covered the window size then substring is found return true
            if j == i + window_size:
                return True

        return False