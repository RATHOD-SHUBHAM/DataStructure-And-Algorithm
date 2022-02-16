'''
First sort width in increasing order : so here we know which envelope will fit in upcoming envelope

Catch is we want only strictly increasing

so, second sort the height in decreasing order. so that larger number will come in front and it wont fit in upcoming envelope

Eg. 23 , 25, 26 -> they have same width. now sorting the height based on decreasing height

26 , 25 ,23 . see now we know 26 wont fit in 25 and 23.

https://leetcode.com/problems/russian-doll-envelopes/discuss/1775970/Longest-Increasing-SubsequenceLIS-or-Python-or-2-Solution
'''
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x : (x[0], -x[1])) # first sort the first index. if there is a conflict. sort the second index
        print(envelopes)
        
        lis = []
        
        for env in envelopes:
            _,h = env
            left = self.binarySearch(lis,h)
            
            if len(lis) == left:
                lis.append(h)
            else:
                lis[left] = h
        
        return len(lis)
    
    def binarySearch(self,lis,h):
        left = 0
        right = len(lis) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if lis[mid] == h:
                return mid
            elif lis[mid] < h:
                left = mid + 1
            else:
                right = mid - 1
        return left
        
                