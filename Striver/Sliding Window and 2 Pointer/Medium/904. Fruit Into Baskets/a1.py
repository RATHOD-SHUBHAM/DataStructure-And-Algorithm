# ---------------- Brute Force ----------------------

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
    

# ---------------- Sliding Window ----------------------

# Tc: O(n) | Sc: O(1)

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)

        max_picked = 0

        dic = collections.defaultdict(int) # keep track of frequency

        left  = right = 0

        while right < n:
            dic[fruits[right]] += 1

            while len(dic) > 2:
                dic[fruits[left]] -= 1

                if dic[fruits[left]] == 0:
                    del dic[fruits[left]]
                
                left += 1

            cur_picked = right - left + 1
            max_picked = max(cur_picked, max_picked)
            
            right += 1

        return max_picked