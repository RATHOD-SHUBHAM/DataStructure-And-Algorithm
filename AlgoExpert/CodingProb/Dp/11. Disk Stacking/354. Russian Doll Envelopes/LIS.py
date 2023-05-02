# sort + LIS
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        
        # sort the envelope if there is a conflict sort height in decreasing order
        envelopes.sort(key = lambda x:(x[0], -x[1]))
        # print(envelopes)
        
        
        # perform LIS on height - since width is already sorted
        envelope = [x[1] for x in envelopes]
        # print(envelope)
        
        def LIS(left, right, target):
            nonlocal res
            
            # base case
            if left == right:
                return left
            
            mid = left + (right - left) // 2
            
            if res[mid] == target:
                return mid
            elif res[mid] < target:
                return LIS(mid + 1, right , target)
            else:
                return LIS(left , mid , target)
        
        # store the LIS
        res = []
        
        for env in envelope:
            if not res or res[-1] < env:
                res.append(env)
                continue
            
            idx = LIS(0 , len(res) - 1, env)
            
            res[idx] = env
            
        # print(res)
        return len(res)