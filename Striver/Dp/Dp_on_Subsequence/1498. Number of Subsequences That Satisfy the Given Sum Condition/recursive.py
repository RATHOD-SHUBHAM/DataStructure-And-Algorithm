class Solution:
    def __init__(self):
        self.count = 0

    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Logic
        def recursion(idx, st):
            # base case
            if idx < 0:
                if st:
                    min_val = min(st)
                    max_val = max(st)

                    if (max_val + min_val) <= target:
                        self.count += 1
                
                return
            
            # take
            st.append(nums[idx])
            recursion(idx-1, st)

            # dont take
            st.pop()
            recursion(idx-1, st)


        idx = n - 1
        st = []
        recursion(idx, st)

        return self.count