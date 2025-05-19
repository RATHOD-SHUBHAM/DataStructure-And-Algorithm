# ------------------------------------- Brute Force ------------------------------------- #
class Solution:
    def __init__(self):
        self.result = []
    def isSubsetSum (self, arr, summ):
        # code here
        n = len(arr)
        
        def dfs(i, st):
            if i == n:
                self.result.append(st[::])
                return
        
            # Include the current element
            st.append(arr[i])
            dfs(i+1,st)
            
            # Donot include the current element
            st.pop()
            dfs(i+1,st)
        
        i = 0
        st = []
        dfs(i,st)
        
        for subset in self.result:
            if sum(subset) == summ:
                return True
        return False
    
if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    # summ = 9
    summ = 30
    # arr = [1,2,3]
    # summ = 6
    obj = Solution()
    print(obj.isSubsetSum(arr, summ))

# ------------------------------------- Better Brute Force ------------------------------------- #
class Solution:
    def isSubsetSum (self, arr, summ):
        # code here
        n = len(arr)
        
        def dfs(i, st):
            if i == n:
                curSum = sum(st)
                if curSum == summ:
                    return 1
                else:
                    return 0
        
            # Include the current element
            st.append(arr[i])
            if dfs(i+1, st) == 1:
                return 1
            
            # Donot include the current element
            st.pop()
            if dfs(i+1, st) == 1:
                return 1
        
        i = 0
        st = []
        if dfs(i, st) == 1:
            return True
        else:
            return False
        

if __name__ == "__main__":
    # arr = [3, 34, 4, 12, 5, 2]
    # summ = 9
    # summ = 30
    arr = [1,2,3]
    summ = 6
    obj = Solution()
    print(obj.isSubsetSum(arr, summ))

# ------------------------------------- Recursion -------------------------------------
class Solution:
    def isSubsetSum (self, arr, sum):
        n = len(arr)
        
        idx = n - 1
        
        return self.recursion(idx, arr, sum)
    
    def recursion(self, idx, arr, target):
        # base case
        if idx < 0:
            return False
        
        if target == 0:
            return True
        
        # Take
        if target >= arr[idx]:
            take = self.recursion(idx - 1, arr, target - arr[idx])
        else:
            take = False
        
        
        # Dont take
        dont_take = self.recursion(idx - 1, arr, target)
        
        return take or dont_take
    

# ------------------------------------- Memoization ------------------------------------- #
class Solution:
    def isSubsetSum (self, arr, sum):
        n = len(arr)
        
        idx = n - 1
        
        memo = {}
        
        return self.recursion(idx, memo, arr, sum)
    
    def recursion(self, idx, memo, arr, target):
        # base case
        if idx < 0:
            return False
        
        if target == 0:
            return True
        
        if (idx, target) in memo:
            return memo[(idx, target)]
        
        # Take
        if target >= arr[idx]:
            take = self.recursion(idx - 1, memo, arr, target - arr[idx])
        else:
            take = False
        
        
        # Dont take
        dont_take = self.recursion(idx - 1, memo, arr, target)
        
        memo[(idx, target)] = take or dont_take
        
        return memo[(idx, target)]
    
# ------------------------------------- Tabulation -------------------------------------
class Solution:
    def isSubsetSum (self, arr, sum):
        # code here
        n = len(arr)
        
        dp = [[False for _ in range(sum+1)]for _ in range(n)]
        
        # Base case: empty subset can form sum = 0
        for i in range(n):
            dp[i][0] = True
        
        if sum >= arr[0]:
            dp[0][arr[0]] = True
        
        for idx in range(1, n):
            for target in range(1, sum+1):
                if target >= arr[idx]:
                    take = dp[idx-1][target - arr[idx]]
                else:
                    take = False
                
                dont_take = dp[idx-1][target]
                
                dp[idx][target] = take or dont_take
        
        return dp[n-1][sum]
    
# ------------------------------------- Space Optimization -------------------------------------
class Solution:
    def isSubsetSum (self, arr, sum):
        # code here
        n = len(arr)
        
        dp = [False for _ in range(sum+1)]
        
        # Base case: empty subset can form sum = 0
        dp[0] = True
        
        if sum >= arr[0]:
            dp[arr[0]] = True
        
        for idx in range(1, n):
            temp = [False for _ in range(sum+1)]
            
            for target in range(1, sum+1):
                if target >= arr[idx]:
                    take = dp[target - arr[idx]]
                else:
                    take = False
                
                dont_take = dp[target]
                
                temp[target] = take or dont_take
            
            dp = temp
            dp[0] = True
        
        return dp[sum]

# ------------------------------------- ----------- -------------------------------------