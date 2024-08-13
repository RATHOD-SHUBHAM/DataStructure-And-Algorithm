# Tc: O(n^2) | Sc: O(n)

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)

        max_picked = 0

        left  = 0

        while left < n:

            right = left
            
            picked = set()
            
            while right < n:

                picked.add(fruits[right])

                if len(picked) > 2:
                    break
                
                right += 1
            
            cur_picked = right - left
            max_picked = max(max_picked, cur_picked)

            left += 1
        
        return max_picked