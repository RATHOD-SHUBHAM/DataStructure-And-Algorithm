# Monotonous stack
# Tc: O(m+n)
# Sc: O(n)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nge = [-1] * len(nums1) 
        
        # create a hashmap for index and val for nums1
        # lookup time is faster rather than iterating it always.
        dic = {val : idx for idx, val in enumerate(nums1)}
        # print(dic)
        
        for i in reversed(range(len(nums2))):
            # check if the val is in nums1
            if nums2[i] in dic:
                # get idx
                idx = dic[nums2[i]]
                
                while stack and stack[-1] <= nums2[i]:
                    stack.pop()
                    
                # after popping out all the small value
                # if there is a element present in stack than that is the greater element
                if stack:
                    nge[idx] = stack[-1] 
                # if nothing is present than -1
                else:
                    nge[idx] = -1
                    
            stack.append(nums2[i])
            
        return nge
        