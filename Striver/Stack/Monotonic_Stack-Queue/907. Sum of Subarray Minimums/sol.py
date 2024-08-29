from typing import List

class Solution:
    def getPSEE(self, arr, n):
        '''
            Previous Smaller or Equal Element
        '''
        stack = []

        op = [-1] * n

        for i in range(n):
            cur_ele = arr[i]

            while stack and cur_ele < arr[stack[-1]]:
                stack.pop()
            
            if not stack:
                op[i] = -1
            else:
                op[i] = stack[-1]
            
            stack.append(i)
        
        return op
            


    def getNSE(self,arr, n):
        '''
            Next Smaller Element
        '''
        stack = [] # Monotonic stack

        op = [-1] * n

        for i in reversed(range(n)):
            cur_ele = arr[i]

            while stack and cur_ele <= arr[stack[-1]]:
                stack.pop()
            
            if not stack:
                op[i] = n # this should be pointing to nth index
            else:
                op[i] = stack[-1]
            
            stack.append(i)
        
        # print(op)
        return op


    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = (10 ** 9) + 7

        # Find the PSEE and NSE
        psee = self.getPSEE(arr, n)
        # print(psee)
        nse = self.getNSE(arr, n)
        # print(nse)

        sum_of_subarray = 0

        for i in range(n):
            cur_ele = arr[i]

            # Individual Contribution
            idx_of_PSEE = psee[i]
            idx_of_NSE = nse[i]

            
            # Calculate the subarray len
            left_subarray_len = i - idx_of_PSEE
            right_subarray_len = idx_of_NSE - i
            subarray_len = left_subarray_len * right_subarray_len

            # Get the individual contribution
            individual_contri = (cur_ele * subarray_len)

            # Add the individual contribution to total contribution count
            sum_of_subarray = (sum_of_subarray + individual_contri) % MOD
        
        
        return sum_of_subarray