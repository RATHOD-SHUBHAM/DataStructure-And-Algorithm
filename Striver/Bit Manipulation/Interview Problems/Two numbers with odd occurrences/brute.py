from collections import Counter
class Solution:
    def twoOddNum(self, Arr, N):
        counter = Counter(Arr)
        
        odd_num = []
        for item, count in counter.items():
            if count % 2 == 1:
                odd_num.append(item)
        
        odd_num = sorted(odd_num)
        return odd_num[::-1]