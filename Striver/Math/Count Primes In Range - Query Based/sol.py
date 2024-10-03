class Solution:
    def seive(self, n):
        ref = [1] * (n+1)
        
        i = 2
        while i * i <= n:
            if ref[i] == True:
                x = i * i
                for j in range(x, n+1, i):
                    ref[j] = 0
            
            i += 1
        
        return ref
    
    def countPrimes(self,n, query):
        #code here
        max_val = 2
        for q in query:
            _, r = q 
            max_val = max(max_val, r)
        
        ref = self.seive(max_val)
        print(ref)
        
        # get prefix sum
        for i in range(3, max_val + 1):
            ref[i] = ref[i-1] + ref[i]
        
        ref[0] = 0
        ref[1] = 0
        print(ref)

        # Compute prefix sum count
        prefix_sum = []
        for l, r in query:
            prefix_r = ref[r]
            prefix_l = ref[l-1]
            prefix_sum.append(prefix_r - prefix_l)
        
        print(prefix_sum)
        return prefix_sum


if __name__ == '__main__':
    obj = Solution()

    n = 3
    # query = [[3, 10], [8,20], [1,5]]
    query = [[3, 13], [2,29], [8,17]]
    obj.countPrimes(n, query)