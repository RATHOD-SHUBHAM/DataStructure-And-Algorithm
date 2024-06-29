class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        ans = []

        for i in range(n):
            xor = 0
            left, right = queries[i]

            while left <= right:
                '''
                    XOR of the entire window frame.
                '''
                xor ^= arr[left]
                left += 1
            
            ans.append(xor)
        
        return ans
