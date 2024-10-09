# Tc: O(n log n)

class Solution:
    def count_set_bits(self, x):
        count = 0
        
        while x > 0:
            if x & 1 != 0:
                count += 1
            
            x = x >> 1
        
        if x == 1:
            count += 1
        
        return count
    
    def countBits(self, n: int) -> List[int]:
        result = [0]
        
        # Tc: O(n)
        for i in range(1, n+1):
            set_bits = self.count_set_bits(i) # Tc: O(log n)
            result.append(set_bits)
        
        return result

# ---------------------------------------------------------------------------

