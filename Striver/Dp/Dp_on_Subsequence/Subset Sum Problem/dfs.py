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