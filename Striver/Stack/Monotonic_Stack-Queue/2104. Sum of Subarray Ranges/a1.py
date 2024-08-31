# Tc: O(n^2) | Sc: O(1)

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        total = 0

        for i in range(n):
            for j in range(i, n):
                smallest = min(nums[i : j + 1])
                largest = max(nums[i : j + 1])
                total += (largest - smallest)
        
        return total

# ------------------ Monotonic Stack ------------------

# Tc and Sc: O(n)

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
    
    def subarray_range_minimum(self, nums, n):
        psee = self.PSEE(nums, n)
        # print(psee)
        nse = self.NSE(nums, n)
        # print(nse)

        summation_min_val = 0

        for i in range(n):
            cur_ele = nums[i]

            left_sub_array = i - psee[i]
            right_sub_array = nse[i] - i

            subarray_len = left_sub_array * right_sub_array

            # Individual Contribution
            indi_contri = (subarray_len * cur_ele)

            summation_min_val += indi_contri
        
        return summation_min_val
    
    def subarray_range_maximum(self, nums, n):
        pgee = self.PGEE(nums, n)
        nge = self.NGE(nums, n)
        
        summation_max_val = 0

        for i in range(n):
            cur_ele = nums[i]

            left_sub_array = i - pgee[i]
            right_sub_array = nge[i] - i

            subarray_len = left_sub_array * right_sub_array

            # Individual Contribution
            indi_contri = (subarray_len * cur_ele)

            summation_max_val += indi_contri
        
        return summation_max_val


    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        summation_min_val = self.subarray_range_minimum(nums, n)
        summation_max_val = self.subarray_range_maximum(nums, n)

        return summation_max_val - summation_min_val