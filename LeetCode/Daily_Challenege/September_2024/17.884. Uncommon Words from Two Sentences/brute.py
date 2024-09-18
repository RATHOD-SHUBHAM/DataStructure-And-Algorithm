class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        list_s1 = s1.split(' ')
        list_s2 = s2.split(' ')

        set_1 = collections.Counter(list_s1)
        set_2 = collections.Counter(list_s2)

        op = []

        for ch in list_s1:
            if set_1[ch] <= 1 and ch not in set_2:
                op.append(ch)
        
        for ch in list_s2:
            if set_2[ch] <= 1 and ch not in set_1:
                op.append(ch)
        
        return op