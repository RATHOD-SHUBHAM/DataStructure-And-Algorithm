'''
2- pointer:
    Lock the position where we want to insert : 
    we want to insert right after the unique number
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        swap_idx = 0
        i = 1

        # while i < n:
        #     if nums[i - 1] != nums[i]:
        #         self.swap(i-1, swap_idx, nums)
        #         swap_idx += 1
        #         i += 1
        #     else:
        #         i += 1
        
        while i < n:
            if nums[i - 1] != nums[i]:
                self.swap(i-1, swap_idx, nums)
                swap_idx += 1
            
            i += 1
        
        self.swap(n-1, swap_idx, nums)

        # print(nums)
        # print(nums[ :swap_idx + 1])
        # return len(nums[ :swap_idx + 1]) # or return swap_idx + 1
        return swap_idx + 1
    
    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]
        
        

            
            



        