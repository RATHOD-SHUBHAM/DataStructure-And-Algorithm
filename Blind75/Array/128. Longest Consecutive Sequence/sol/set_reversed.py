'''
    Set + reverse search
'''
# Sc: O(n) | Tc : O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_sequence = 0

        for n in set_nums:
            # check if this is the starting number
            if n-1 not in set_nums:
                current_streak = 1
                current_num = n

                while current_num + 1 in set_nums:
                    current_streak += 1
                    current_num += 1

                max_sequence = max(max_sequence, current_streak)

        return  max_sequence             
