# Idea is -> A negative number can decrease the score
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        # bring all positive in front to increase the score
        sorted_num = sorted(nums, reverse = True)
        # print(sorted_num)

        cur_score = max_score = 0

        for i in range(n):
            if sorted_num[i] < 0:
                return max_score
            
            cur_score += sorted_num[i]
            max_score = max(max_score, cur_score)
        
        return max_score

"""
# Analysis of why this answer is wrong:

Intuition about negative numbers is partially correct, but you're missing a crucial detail about how prefix sums work.

Let me clarify the difference between what you're thinking and what the problem is actually asking:
- What you're thinking:
    "Take only positive numbers to maximize the count of positive values"

- What the problem actually wants:
    "Maximize the count of positive prefix sums"
"""

# ---------------------  Correct Approach ----------------------


# The score of nums is the number of positive integers in the array prefix
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        # bring all positive in front to increase the score
        sorted_num = sorted(nums, reverse = True)
        # print(sorted_num)

        prefix_sum = score = 0

        for i in range(n):
            prefix_sum += sorted_num[i]

            if prefix_sum > 0:
                score += 1
            else:
                # the prefix sum will only decrease because we have sorted the array
                return score      
        
        return score