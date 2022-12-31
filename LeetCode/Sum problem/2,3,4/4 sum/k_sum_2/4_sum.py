# Tc and Sc: O(n^2)

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        summ = collections.defaultdict(int)
        
        for a in nums1:
            for b in nums2:
                cur_sum = a + b
                summ[cur_sum] += 1
                
        # print(summ)
        
        count = 0
        for c in nums3:
            for d in nums4:
                cur_sum = c + d
                # print(cur_sum)
                # a+b = -(c+d)
                if summ[-cur_sum]:
                    # there can be multiple combination that would give the cur_sum
                    count += summ[-cur_sum]
                    
        return count
                