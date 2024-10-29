"""
After you solve 4Sum, an interviewer can follow-up with 5Sum II, 6Sum II, and so on. 
What they are really expecting is a generalized solution for k input arrays.
"""

from collections import Counter
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        group_list = [nums1, nums2, nums3, nums4] # this group can be of k len
        
        k = len(group_list) // 2
        
        left_half_group = group_list[ : k]
        right_half_group = group_list[k : ]
        print(left_half_group)
        # print(right_half_group)
        
        # Count of a+b
        a = self.k_sum_count(left_half_group)
        print("a: ", a)
        # Count of c+d
        b = self.k_sum_count(right_half_group)
        print("b",b)
        
        # count the number of combination (a+b)-(c+d) = 0
        no_of_combinations = 0
        for _sum in a:
            left_sum = a[_sum]
            right_sum = b[-_sum] if -_sum in b else 0
            
            no_of_combinations += left_sum * right_sum
            
        return no_of_combinations
    
    def k_sum_count(self, half_group):
        prev_sum_count = {0 : 1} # keep track of sum & their number of occurance(Count)
        
        for lst in half_group:
            cur_sum_count = {}
            
            for num in lst:
                for prev_sum in prev_sum_count:
                    cur_sum = num + prev_sum # new_key= a + b
                    
                    if cur_sum not in cur_sum_count:
                        cur_sum_count[cur_sum] = 0
                    
                    cur_sum_count[cur_sum] += prev_sum_count[prev_sum] # new value = count of a + count of b
                    
            prev_sum_count = cur_sum_count
            # print(prev_sum_count)
            
        return prev_sum_count
            
            
        
            