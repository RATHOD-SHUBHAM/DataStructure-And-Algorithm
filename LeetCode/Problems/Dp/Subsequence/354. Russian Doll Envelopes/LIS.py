# Tc : O(nlogn) |sc: O(n)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        '''
        Consider an input [[1, 3], [1, 4], [1, 5], [2, 3]]
        
        If we simply sort and extract the second dimension we get [3, 4, 5, 3], which implies that we can fit three envelopes (3, 4, 5). The problem is that we can only fit one envelope, since envelopes that are equal in the first dimension can't be put into each other.

In order fix this, we don't just sort increasing in the first dimension - we also sort decreasing on the second dimension, so two envelopes that are equal in the first dimension can never be in the same increasing subsequence.
        
        
        
        '''
        envelopes.sort(key = lambda x : (x[0], -x[1]))
        print(envelopes)
        
        envelope = [x[1] for x in envelopes]
        print(envelope)
        
        res = []
        
        def binarySearch(l , r, target):
            nonlocal res , n
            
            # base case
            if l == r:
                return l
            
            mid = l + (r - l) // 2
            
            if res[mid] == target:
                return mid
            elif res[mid] < target:
                return binarySearch(mid + 1, r , target)
            else:
                return binarySearch(l , mid , target)
            

        
        for env in envelope:

            if not res or res[-1] < env:
                res.append(env)
                continue

            idx = binarySearch(0 , len(res) - 1, env)

            res[idx] = env
        
        print(res)
        return len(res)
        
        