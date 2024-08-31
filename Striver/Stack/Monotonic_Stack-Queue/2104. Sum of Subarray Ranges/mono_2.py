'''
Study Mono.py

this is a bit less readable
'''

class Solution:
    def PSEE(self, nums, n):
        '''
            Previous Smaller and Equal Element
        '''
        op = [-1] * n
        stack = []

        for i in range(n):
            cur_ele = nums[i]

            while stack and cur_ele <= nums[stack[-1]]:
                stack.pop()
            
            if not stack:
                op[i] = -1
            else:
                op[i] = stack[-1]
        
            stack.append(i)
        
        return op
    

    def NSE(self, nums, n):
        '''
        Next Smaller Element
        '''

        op = [-1] * n
        stack = []

        for i in reversed(range(n)):
            cur_ele = nums[i]

            while stack and cur_ele < nums[stack[-1]]:
                stack.pop()
            
            if not stack:
                op[i] = n
            else:
                op[i] = stack[-1]
            
            stack.append(i)
        
        return op
    
    def PGEE(self, nums, n):
        '''
        Previous Greater Equal Element
        '''

        op = [-1] * n
        stack = []

        for i in range(n):
            cur_ele = nums[i]

            while stack and cur_ele >= nums[stack[-1]]:
                stack.pop()
            
            if not stack:
                op[i] = -1
            else:
                op[i] = stack[-1]
            
            stack.append(i)
        
        return op

    
    def NGE(self, nums, n):
        '''
        Next Greatest Element
        '''

        op = [-1] * n
        stack = []

        for i in reversed(range(n)):
            cur_ele = nums[i]

            while stack and cur_ele > nums[stack[-1]]:
                stack.pop()
            
            if not stack:
                op[i] = n
            else:
                op[i] = stack[-1]
            
            stack.append(i)
        
        return op
    

    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        summation_min_val = 0
        # Subarry sum range minimum
        psee = self.PSEE(nums, n)
        nse = self.NSE(nums, n)

        summation_max_val = 0
        # Subarry sum range maximum
        pgee = self.PGEE(nums, n)
        nge = self.NGE(nums, n)

        for i in range(n):
            cur_ele = nums[i]

            # Subarry sum range minimum
            min_left_sub_array = i - psee[i]
            min_right_sub_array = nse[i] - i

            min_subarray_len = min_left_sub_array * min_right_sub_array

            min_indi_contri = (min_subarray_len * cur_ele)

            summation_min_val += min_indi_contri

            # Subarry sum range maximum
            max_left_sub_array = i - pgee[i]
            max_right_sub_array = nge[i] - i

            max_subarray_len = max_left_sub_array * max_right_sub_array

            max_indi_contri = (max_subarray_len * cur_ele)

            summation_max_val += max_indi_contri


        return summation_max_val - summation_min_val