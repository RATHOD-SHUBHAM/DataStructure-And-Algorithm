from collections import Counter
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # group the nums - it will be easy to divide
        # a + b = 0; a = -b
        group_nums = [nums1, nums2, nums3, nums4]
        
        k = len(group_nums)
        
        group_size = k // 2
        
        left_group = group_nums[ : group_size]
        right_group = group_nums[group_size : ]
        
        a = self.k_sum_count(left_group)
        print("a: ",a)
        b = self.k_sum_count(right_group)
        print("b : ", b)
        
        total_no_of_combination = 0
        for summ in a: # this can be b as well
            a_sum = a[summ]
            # a = -b -> this will be 0
            b_sum = b[-summ] if -summ in b else 0
            
            total_no_of_combination += a_sum * b_sum
        
        return total_no_of_combination
    
    def k_sum_count(self, group_list):
        prev_sum_count = {0 : 1}
        
        # take the first list
        for cur_lst in group_list:
            cur_sum_count = {} # keep track of the cur sum for the cur list
            # add every number to previous sum
            for num in cur_lst:
                for prev_sum in prev_sum_count:
                    cur_sum = num + prev_sum

                    if cur_sum not in cur_sum_count:
                        cur_sum_count[cur_sum] = 0
                    
                    # value represent the number of combination that can form the previous sum
                    # so if we add cur num to prev sum - this is same as adding the cur num to number comination that will form the sum
                    # eg: if there are 2 number which can produce a sum of 0
                    # then add 1 to 0 mean there will be 2 number who will give sum 1 when we add the cur number 1
                    cur_sum_count[cur_sum] += prev_sum_count[prev_sum]
                    
            # once all the combination for cur list is over
            # copy the new sum
            prev_sum_count = cur_sum_count
            
        return prev_sum_count
        