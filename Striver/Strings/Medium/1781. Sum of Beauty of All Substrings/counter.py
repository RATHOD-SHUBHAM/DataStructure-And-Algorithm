import collections

class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)

        beauty = 0

        # go through every substring and calculte frequency
        for i in range(n):
            dic = collections.defaultdict(int)

            for j in range(i, n):
                dic[s[j]] += 1
                
                max_freq = max(dic.values())
                min_freq = min(dic.values())

                beauty += max_freq - min_freq
        
        # print(beauty)
        return beauty