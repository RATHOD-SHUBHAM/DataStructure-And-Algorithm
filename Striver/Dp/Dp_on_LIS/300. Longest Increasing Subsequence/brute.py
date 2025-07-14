class Solution:
    def __init__(self):
        self.max_len = -math.inf
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)    

        def dfs(i, st):
            # base case
            if i == n:
                subseq = st[::]

                for i in range(1, len(subseq)):
                    if subseq[i-1] >= subseq[i]:
                        return

                cur_subseq_len = len(subseq)
                self.max_len = max(self.max_len, cur_subseq_len)
                return 
            
            # Logic
            st.append(nums[i])
            dfs(i+1, st)

            st.pop()
            dfs(i+1, st)

            return 
        
        i = 0
        st = []
        dfs(i, st)

        return self.max_len