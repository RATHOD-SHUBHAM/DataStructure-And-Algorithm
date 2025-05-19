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