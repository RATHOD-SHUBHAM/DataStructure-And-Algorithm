from collections import defaultdict
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        m = len(arr)
        n = len(queries)
        
        # Step 1: prefix_xor
        dic = defaultdict(int)

        xor = 0
        for i in range(m):
            xor ^= arr[i]

            dic[i] = xor
        
        print(dic)

        # Step 2: Get the values in the range
        ans = []
        for i in range(n):
            left , right = queries[i]
            
            if left > 0:
                total_xor = dic[right] ^ dic[left - 1]
            else:
                total_xor = dic[right]
            
            ans.append(total_xor)
        
        return ans
    
# -------------------- Optimal --------------------

from collections import defaultdict
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        m = len(arr)
        n = len(queries)
        
        # Step 1: prefix_xor
        dic = defaultdict(int)

        xor = 0
        for i in range(m):
            xor ^= arr[i]

            dic[i] = xor
        
        print(dic)

        # Step 2: Get the values in the range
        ans = []
        for i in range(n):
            left , right = queries[i]
            total_xor = 0

            total_xor ^= dic[right]

            if left > 0:
                total_xor ^= dic[left - 1]
            
            ans.append(total_xor)
        
        return ans

# -------------------- Same Solution --------------------

from collections import defaultdict
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        m = len(arr)
        n = len(queries)
        
        # Step 1: prefix_xor
        dic = defaultdict(int)

        xor = 0
        for i in range(m):
            xor ^= arr[i]

            dic[i] = xor
        
        print(dic)

        # Step 2: Get the values in the range
        ans = []
        for i in range(n):
            left , right = queries[i]
            
            if left > 0:
                '''
                    If left is grater than zero, remove the previous xor
                '''
                total_xor = dic[right] ^ dic[left - 1]
            else:
                total_xor = dic[right]
            
            ans.append(total_xor)
        
        return ans