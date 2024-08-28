class Solution:
    def count_NGEs(self, N, arr, queries, indices):
        n = len(indices)
        
        op = [None] * n
        
        for i in reversed(range(n)):
            count = 0
            
            idx = indices[i]
            j = len(arr) - 1
            
            
            while j > idx:
                cur_num = arr[j]
                cur_num_at_idx = arr[idx]
                
                if cur_num > cur_num_at_idx:
                    count += 1
                
                j -= 1
            
            op[i] = count
        
        return op