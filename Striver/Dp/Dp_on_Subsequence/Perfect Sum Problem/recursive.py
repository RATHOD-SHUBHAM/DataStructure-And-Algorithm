class Solution:
    def perfectSum(self, arr, target):
        # code here
        n = len(arr)
        
        def recursion(idx, cur_sum):
            if idx < 0:
                if cur_sum == target:
                    return 1
                else:
                    return 0
            
            take = recursion(idx - 1, cur_sum + arr[idx])
            no_take = recursion(idx - 1, cur_sum)
            
            return take + no_take
            
        idx = n - 1
        cur_sum = 0
        
        return recursion(idx, cur_sum)
    
# --------------------------- Same Solution with different approach ---------------------------

#User function Template for python3
class Solution:
    def perfectSum(self, arr, target):
        # code he
        n = len(arr)
        
        idx = n - 1
        
        return self.recursion(idx, n, arr, target)

    def recursion(self, idx, n, arr, target):
        # base case
        if idx < 0:
            if target == 0:
                return 1
            else:
                return 0

        # Logic
        if target >= arr[idx]:
            take = self.recursion(idx - 1, n, arr, target - arr[idx])
        else:
            take = 0
            
        no_take = self.recursion(idx - 1, n, arr, target)
        
        return take + no_take

