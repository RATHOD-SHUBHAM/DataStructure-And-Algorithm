# TC and Sc: O(n)

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        starting_Score = 0
        
        neg_nums = [-x for x in nums]
        heapq.heapify(neg_nums)
        
        while k > 0:
            max_val = heapq.heappop(neg_nums)
            max_val *= -1
            
            starting_Score += max_val
            replace_val = ceil(max_val / 3)
            heapq.heappush(neg_nums,(replace_val * -1))
            
            k -= 1
        
        return starting_Score
        