## LCS : Longest Consecutive Sequence.

# Brute Force.

# Tc: O(n^3) | Sc: O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_sequence = -math.inf

        # O(n)
        for n in nums:
            cur_ele = n
            next_ele = cur_ele + 1

            cur_sequence = 1

            '''
                Loop runs through all the input everytime we increase the next element count
                O(n^2)
            '''
            while next_ele in nums:
                cur_sequence += 1
                next_ele += 1

            max_sequence = max(max_sequence , cur_sequence)
        
        return max_sequence


 # ------------------------------------------------------------------------
 # 
 # Sorting
 # 
 # # Tc: O(nlogn) | Sc: O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        i = 0
        n = len(nums)

        max_sequence = -math.inf

        while i < n:
            j = i
            cur_size = 1

            cur_ele = nums[i]
            next_ele = cur_ele + 1
            # print(next_ele)

            while j+1 < n and next_ele == nums[j+1]:
                cur_size += 1

                cur_ele = next_ele
                next_ele = cur_ele + 1

                j += 1
                # print("j : ",j)
            
            max_sequence = max(max_sequence , cur_size)

            i = j + 1
            # print("i : ", i)

        return max_sequence
              

# ------------------------------------------------------------------------

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
