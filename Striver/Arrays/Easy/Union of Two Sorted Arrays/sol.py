# Tc: O(nlogn) | Sc: O(m + n)
class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        union_set = set()
        
        _n = max(m,n)
        
        for i in range(_n):
            if i < n:
                union_set.add(arr1[i])
            if i < m:
                union_set.add(arr2[i])

        return sorted(list(union_set))